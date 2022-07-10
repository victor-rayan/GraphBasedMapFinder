import heapq
import pygame as pg

'''
Algoritmos utilizados para traçar a menor rota no grid
'''

vec = pg.math.Vector2


class DijkstraAlgorithm:

    def transform_int(v):
        return (int(v.x), int(v.y))

    def dijkstra_search(graph, start, end):
        frontier = PriorityQueue()
        frontier.put(DijkstraAlgorithm.transform_int(start), 0)
        path = {}
        cost = {}
        path[DijkstraAlgorithm.transform_int(start)] = None
        cost[DijkstraAlgorithm.transform_int(start)] = 0

        while not frontier.empty():
            current = frontier.get()
            if current == end:
                break
            for next in graph.neighbors(vec(current)):
                next = DijkstraAlgorithm.transform_int(next)
                next_cost = cost[current] + graph.cost(current, next)
                if next not in cost or next_cost < cost[next]:
                    cost[next] = next_cost
                    priority = next_cost
                    frontier.put(next, priority)
                    path[next] = vec(current) - vec(next)
        # print (path)
        return path


class PriorityQueue:
    def __init__(self):
        self.nodes = []

    def put(self, node, cost):
        heapq.heappush(self.nodes, (cost, node))

    def get(self):
        return heapq.heappop(self.nodes)[1]

    def empty(self):
        return len(self.nodes) == 0
