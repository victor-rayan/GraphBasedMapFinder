import pygame as pg
import heap as hp
import const as c
import grid as g
from os import path
from grid import *

vec = pg.math.Vector2

pg.init()
sc = pg.math.Vector2
screen = pg.display.set_mode((c.WIDTH, c.HEIGHT ))
clock = pg.time.Clock()

# Imagem mapa do jogo
gtasa_img = pg.image.load('gtasa.jpg').convert_alpha()
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

def draw_icons():
    start_center = (goal.x * c.TILE + c.TILE / 2, goal.y * c.TILE + c.TILE / 2)
    screen.blit(home_img, home_img.get_rect(center=start_center))
    goal_center = (start.x * c.TILE + c.TILE / 2, start.y * c.TILE + c.TILE / 2)
    screen.blit(cross_img, cross_img.get_rect(center=goal_center))

def transform_int(v):
    return (int(v.x), int(v.y))

def dijkstra_search(graph, start, end):
    frontier = hp.PriorityQueue()
    frontier.put(transform_int(start), 0)
    path = {}
    cost = {}
    path[transform_int(start)] = None
    cost[transform_int(start)] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == end:
            break
        for next in graph.neighbors(vec(current)):
            next = transform_int(next)
            next_cost = cost[current] + graph.cost(current, next)
            if next not in cost or next_cost < cost[next]:
                cost[next] = next_cost
                priority = next_cost
                frontier.put(next, priority)
                path[next] = vec(current) - vec(next)
    # print (path)
    return path

  
icon_dir = path.join(path.dirname(__file__), '../icons')

# Imagens das ferraduras
horse_img = pg.image.load(path.join(icon_dir, 'horse.png')).convert_alpha()
horse_img = pg.transform.scale(horse_img, (40, 40))
horse_rect= horse_img.get_rect()
horse_rect.center = (70 * c.TILE + c.TILE / 2, 65 * c.TILE + c.TILE / 2)


# Imagens origem
home_img = pg.image.load(path.join(icon_dir, 'home.png')).convert_alpha()
home_img = pg.transform.scale(home_img, (30, 30))
home_img.fill((0, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)

# Imagens destino
cross_img = pg.image.load(path.join(icon_dir, 'cross.png')).convert_alpha()
cross_img = pg.transform.scale(cross_img, (30, 30))

# Caminho que o gps percorre
paths_gps = {}
gps = pg.image.load(path.join(icon_dir, 'path.png')).convert_alpha()
gps = pg.transform.scale(gps, (20, 20)) 
gps.fill(('blue'), special_flags=pg.BLEND_RGBA_MULT)

for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    paths_gps[dir] = pg.transform.rotate(gps, vec(dir).angle_to(vec(1, 0)))  

with open('collisionsList.txt', 'r') as file:
    data = file.read().replace('\n', '')

res = eval(data)

walls = res 
print(type(walls))    
goal = vec(1, 1)
start = vec(1, 2)
path = dijkstra_search(source, goal, start)

for wall in walls:
    source.walls.append(vec(wall))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()     
        if event.type == pg.MOUSEBUTTONDOWN:
            mouseposition = sc(pg.mouse.get_pos()) // c.TILE
            print(mouseposition)
            if event.button == 1:
                if mouseposition in source.walls:
                    source.walls.remove(mouseposition)
                    print(mouseposition)
                else:
                    source.walls.append(mouseposition)
            if event.button == 2:
                start = mouseposition
                print(mouseposition)
                print('esiu')
            if event.button == 3:
                print('entrou')
                goal = mouseposition
            path = dijkstra_search(source, goal, start)       


    screen.fill("black")
    screen.blit(gtasa_img, gtasa_rect)
    screen.blit(horse_img, horse_rect)
   
    # draw_grid()
    # source.draw()

    try:
        current = start + path[transform_int(start)]
        while current != goal:
            x = current.x * c.TILE + c.TILE / 2
            y = current.y * c.TILE + c.TILE / 2
            img = paths_gps[transform_int(path[(current.x, current.y)])]
            r = img.get_rect(center=(x, y))
            screen.blit(img, r)
            current = current + path[transform_int(current)]
    except KeyError:
        print('erro')

    draw_icons()
    pg.display.flip()