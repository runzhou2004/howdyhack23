

from typing import Optional, Protocol, TypeVar
import collections
import heapq
import math



Location = TypeVar('Location')
class Graph(Protocol):
    def neighbors(self, id: Location) -> list[Location]: pass

class SimpleGraph:
    def __init__(self):
        self.edges: dict[Location, list[Location]] = {}
    
    def neighbors(self, id: Location) -> list[Location]:
        return self.edges[id]
    
    def cost(self, fromNode, toNode):
        return 
    
class PriorityQueue:
    def __init__(self):
        self.elements: list[tuple[float]] = []
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    

class WeightedGraph(Graph):
    def cost(self, from_id: Location, to_id: Location) -> float: pass


GridLocation = tuple[float, float]

class GridWithWeights(SimpleGraph):
    def __init__(self):
        super().__init__()
    
    def cost(self, from_node: GridLocation, to_node: GridLocation) -> float:
        return math.sqrt((to_node[0] - from_node[0])**2 + (to_node[1] - to_node[1])**2)/20



    

busGraph = SimpleGraph()
busGraph.edges = {
    
    'A': [('B', 1)],
    'B': [('C', 2)],
    'C': [('B', 3), ('D', 4), ('F', 5)],
    'D': [('C', 6), ('E', 7)],
    'E': [('F', 8)],
    'F': [],
    
}


def heuristic() -> float:
    return 0

def reconstruct_path(came_from: dict[Location, Location],
                     start: Location, goal: Location) -> list[Location]:

    current: Location = goal
    path: list[Location] = []
    if goal not in came_from: # no path was found
        return []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path



def a_star_search(graph: WeightedGraph, start: Location, goal: Location):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: dict[Location, Optional[Location]] = {}
    cost_so_far: dict[Location, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current: Location = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + next[1]
            if next[0] not in cost_so_far or new_cost < cost_so_far[next[0]]:
                cost_so_far[next[0]] = new_cost
                priority = new_cost + heuristic()
                frontier.put(next[0], priority)
                came_from[next[0]] = current
    
    return came_from, cost_so_far



print('Reachable from A:')
print(reconstruct_path(a_star_search(busGraph, 'A', 'B')[0], 'A', 'B'))
print('Reachable from E:')
print(reconstruct_path(a_star_search(busGraph, 'B', 'E')[0], 'B', 'E'))
print(a_star_search(busGraph, 'A', 'E'))

        
    
    