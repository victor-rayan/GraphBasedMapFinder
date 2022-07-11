import pygame as pg
import const as c
import grid as g
import math
from grid import *
from finder import DijkstraAlgorithm

'''
Tela principal do jogo que contem o mapa utilizado e os algoritmos para traçar a menor rota
'''

def gta_gamehorses(Boolean):

    from os import path
    vec = pg.math.Vector2

    pg.init()
    sc = pg.math.Vector2
    screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
    clock = pg.time.Clock()

    # Imagem mapa do jogo
    gtasa_img = pg.image.load('../assets/gtasa.jpg').convert_alpha()
    gtasa_img = pg.transform.scale(gtasa_img, (c.WIDTH, c.HEIGHT))
    gtasa_rect = gtasa_img.get_rect()
    gtasa_rect.center = c.WIDTH // 2, c.HEIGHT // 2

    ## false == Jetpack
    ## True == car
    typevehicule = Boolean

    source = g.WeightedGrid(c.RESWIDTH, c.RESHEIGHT, typevehicule)

    pg.display.set_caption("GTA Horsehoes")

    icon_dir = path.join(path.dirname(__file__), '../assets')

    # Imagens das ferraduras
    horse_img = pg.image.load(path.join(icon_dir, 'horse.png')).convert_alpha()
    horse_img = pg.transform.scale(horse_img, (43, 43))

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

    def draw_grid():
        for x in range(0, c.WIDTH, c.TILE):
            pg.draw.line(screen, 'blue', (x, 0), (x, c.HEIGHT))
        for y in range(0, c.HEIGHT, c.TILE):
            pg.draw.line(screen, 'blue', (0, y), (c.WIDTH, y))

    def draw_icons():
        goal_center = (goal.x * c.TILE + c.TILE / 2,
                       goal.y * c.TILE + c.TILE / 2)
        screen.blit(cross_img, cross_img.get_rect(center=goal_center))
        start_center = (start.x * c.TILE + c.TILE / 2,
                        start.y * c.TILE + c.TILE / 2)
        screen.blit(home_img, home_img.get_rect(center=start_center))

    def draw_horseicons():
        with open('../assets/horsehoeslocations.txt', 'r') as file:
            horsehoes = file.read().replace('\n', '')

        horsehoes = horsehoes.split("), ")

        for item in horsehoes:
            x = item.strip("[() )]")
            new = x.split(",")
            xx = new[0].strip()
            yy = new[1].strip()
            start_center = (float(xx) * c.TILE + c.TILE / 2,
                            float(yy) * c.TILE + c.TILE / 2)
            screen.blit(horse_img, horse_img.get_rect(center=start_center))

    def colisionsListVerify(posx, posy):

        posx = math.floor(posx)
        posy = math.floor(posy)

        with open('../assets/horsehoeslocations.txt', 'r') as file:
            horsehoes = file.read().replace('\n', '')

        horsehoes = horsehoes.split("), ")

        for item in horsehoes:
            x = item.strip("[() )]")
            new = x.split(",")
            xx = new[0].strip()
            yy = new[1].strip()
            if posx == int(xx) and posy == int(yy):
                flag = 1
                break
            else:
                flag = 0
                continue

        if flag == 1:
            return True
        elif flag == 0:
            return False

    if typevehicule:
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            paths_gps[dir] = pg.transform.rotate(
                gps, vec(dir).angle_to(vec(1, 0)))
    else:
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            paths_gps[dir] = pg.transform.rotate(
                gps, vec(dir).angle_to(vec(1, 0)))

    with open('../assets/collisionsList.txt', 'r') as file:
        data = file.read().replace('\n', '')

    flag2 = 0
    res = eval(data)
    walls = res
    goal = vec(1, 1)
    start = vec(1, 2)
    path = DijkstraAlgorithm.dijkstra_search(source, goal, start)

    if typevehicule:
        for wall in walls:
            source.walls.append(vec(wall))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    return 1

            if event.type == pg.MOUSEBUTTONDOWN:
                mouseposition = sc(pg.mouse.get_pos()) // c.TILE
                if event.button == 2:
                    if mouseposition in source.walls:
                        source.walls.remove(mouseposition)
                    else:
                        source.walls.append(mouseposition)
                if event.button == 1:
                    # if mouseposition
                    start = mouseposition
                if event.button == 3:
                    posx = mouseposition.x
                    posy = mouseposition.y

                    if colisionsListVerify(posx, posy):
                        goal = mouseposition

                path = DijkstraAlgorithm.dijkstra_search(source, goal, start)

        screen.fill("black")
        screen.blit(gtasa_img, gtasa_rect)

        draw_horseicons()

        # draw_grid()
        # source.draw()

        try:
            current = start + path[DijkstraAlgorithm.transform_int(start)]
            while current != goal:
                x = current.x * c.TILE + c.TILE / 2
                y = current.y * c.TILE + c.TILE / 2
                img = paths_gps[DijkstraAlgorithm.transform_int(
                    path[(current.x, current.y)])]
                r = img.get_rect(center=(x, y))
                screen.blit(img, r)
                current = current + \
                    path[DijkstraAlgorithm.transform_int(current)]
        except KeyError:
            pass
        except TypeError:
            pass

        draw_icons()
        pg.display.flip()
