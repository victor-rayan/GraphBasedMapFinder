import const as c
import pygame as pg

'''
Define uma matriz na tela e utiliza para formar o grafo
'''


vec = pg.math.Vector2
sc = pg.math.Vector2
screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))


class Grid:
    def __init__(self, width, height, typevehicule):
        self.width = width
        self.height = height
        self.walls = []
        if typevehicule:
            # Todas direções possíveis de ir up, down, left and right
            self.connections = [sc(1, 0), sc(-1, 0), sc(0, 1), sc(0, -1)]
        else:
            self.connections = [vec(1, 0), vec(-1, 0), vec(0, 1), vec(0, -1)]
            self.connections += [vec(1, 1), vec(-1, 1),
                                 vec(1, -1), vec(-1, -1)]

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
            rect = pg.Rect(wall * c.TILE, (c.TILE, c.TILE))
            pg.draw.rect(screen, 'blue', rect)


class WeightedGrid(Grid):
    def __init__(self, width, height, typevehicule):
        super().__init__(width, height, typevehicule)
        self.weights = {}

    def cost(self, from_node, to_node):
        if (vec(to_node) - vec(from_node)).length_squared() == 1:
            return self.weights.get(to_node, 0) + 10
        else:
            return self.weights.get(to_node, 0) + 14

    def draw(self):
        for wall in self.walls:
            rect = pg.Rect(wall * c.TILE, (c.TILE, c.TILE))
            pg.draw.rect(screen, c.MAGENTA, rect)
        for tile in self.weights:
            x, y = tile
            rect = pg.Rect(x * c.TILE + 3, y * c.TILE +
                           3, c.TILE - 3, c.TILE - 3)
            pg.draw.rect(screen, c.FOREST, rect)
