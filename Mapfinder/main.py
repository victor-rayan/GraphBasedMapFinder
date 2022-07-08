import pygame as pg
import heap as hp
import const as c
import grid as g
vec = pg.math.Vector2

pg.init()
sc = pg.math.Vector2
screen = pg.display.set_mode((c.WIDTH, c.HEIGHT ))
clock = pg.time.Clock()
gtasa_img = pg.image.load('Mapfinder/gtasa.jpg').convert_alpha()
gtasa_img = pg.transform.scale(gtasa_img, (c.WIDTH, c.HEIGHT))
gtasa_rect = gtasa_img.get_rect()
gtasa_rect.center = c.WIDTH // 2, c.HEIGHT // 2
source = g.WeightedGrid(c.RESWIDTH, c.RESHEIGHT)

pg.display.set_caption("GTA Horsehoes")

def draw_grid():
    for x in range(0, c.WIDTH, c.TILE):
        pg.draw.line(screen, 'blue', (x, 0), (x, c.HEIGHT))
    for y in range(0, c.HEIGHT, c.TILE):
        pg.draw.line(screen, 'blue', (0, y), (c.WIDTH, y))

def vec2int(v):
    return (int(v.x), int(v.y))

def dijkstra_search(graph, start, end):
    frontier = hp.PriorityQueue()
    frontier.put(vec2int(start), 0)
    path = {}
    cost = {}
    path[vec2int(start)] = None
    cost[vec2int(start)] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == end:
            break
        for next in graph.neighbors(vec(current)):
            next = vec2int(next)
            next_cost = cost[current] + graph.cost(current, next)
            if next not in cost or next_cost < cost[next]:
                cost[next] = next_cost
                priority = next_cost
                frontier.put(next, priority)
                path[next] = vec(current) - vec(next)
    print (path)
    return path, cost

walls = []

for wall in walls:
    source.walls.append(pg.math.Vector2(wall))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            dijkstra_search(source, vec(4,13), vec(21,62))
            quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouseposition = sc(pg.mouse.get_pos()) // c.TILE
            print(mouseposition)
            if event.button == 1:
                if mouseposition in source.walls:
                    source.walls.remove(mouseposition)
                else:
                    source.walls.append(mouseposition)


    screen.fill("black")
    screen.blit(gtasa_img, gtasa_rect)
    draw_grid()
    source.draw()
    pg.display.flip()