import pygame as pg

TILE = 15
RESWIDTH = 40
RESHEIGHT = 40
WIDTH = TILE * RESWIDTH
HEIGHT = TILE * RESHEIGHT

pg.init()
sc = pg.math.Vector2
screen = pg.display.set_mode((WIDTH, HEIGHT ))
clock = pg.time.Clock()
gtasa_img = pg.image.load('Mapfinder\gtasa.jpg').convert_alpha()
gtasa_rect = gtasa_img.get_rect()
gtasa_rect.center = WIDTH // 2, HEIGHT // 2

pg.display.set_caption("GTA Horsehoes")

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.connections = [sc(1, 0), sc(-1, 0), sc(0, 1), sc(0, -1)] # Todas direções possíveis de ir up, down, left and right

    def limits_grid(self, node):
        return 0 <= node.x < self.width and 0 <= node.y < self.height

    def not_inwalls(self, node):
        return node not in self.walls

    def neighbors(self, node):
        neighbors = [node + connection for connection in self.connections]
        neighbors = filter(self.limits_grid, neighbors)
        neighbors = filter(self.not_inwalls, neighbors)
        return neighbors

    def draw(self):
        for wall in self.walls:
            rect = pg.Rect(wall * TILE, (TILE, TILE))
            pg.draw.rect(screen, 'blue', rect)

def draw_grid():
    for x in range(0, WIDTH, TILE):
        pg.draw.line(screen, 'blue', (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILE):
        pg.draw.line(screen, 'blue', (0, y), (WIDTH, y))

source = Grid(RESWIDTH, RESHEIGHT)

while True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouseposition = sc(pg.mouse.get_pos()) // TILE
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