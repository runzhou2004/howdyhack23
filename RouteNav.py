

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
 'Commons': [('Ross and Bizzell - North', 3)],
 'Ross and Bizzell - North': [('Ross and Ireland - North', 1)],
 'Ross and Ireland - North': [('Asbury Water Tower', 1)],
 'Asbury Water Tower': [('Kleberg', 4)],
 'Kleberg': [('Rec Center', 3), ('Reed Arena/Lot 97', 2)],
 'Rec Center': [('Lot 100 G', 2), ('Kleberg - Inbound', 3)],
 'Lot 100 G': [('Reed Arena', 2)],
 'Reed Arena': [('Kleberg - Inbound', 2)],
 'Kleberg - Inbound': [('MSC - ILCB', 2), ('MSC Bus Stop', 9)],
 'MSC - ILCB': [('Fish Pond', 2), ('MSC', 2)],
 'Fish Pond': [('Ross and Ireland - South', 2)],
 'Ross and Ireland - South': [('Ross and Bizzell (South)', 2)],
 'Ross and Bizzell (South)': [('Southside Rec Center', 5)],
 'Southside Rec Center': [('Lewis Street', 2)],
 'Lewis Street': [('Commons', 2)],
 'MSC': [('Beutel', 3), ('Kleberg', 4)],
 'Beutel': [('Wehner', 3)],
 'Wehner': [('School of Public Health', 8)],
 'School of Public Health': [('White Creek 1', 2)],
 'White Creek 1': [('Lot 101', 1)],
 'Lot 101': [('NCTM', 3)],
 'NCTM': [('VTED', 2)],
 'VTED': [('Houston Building', 1)],
 'Houston Building': [('White Creek Community Center', 1)],
 'White Creek Community Center': [('School of Public Health - Inbound', 1)],
 'School of Public Health - Inbound': [('Wehner - Inbound', 6)],
 'Wehner - Inbound': [('MSC', 5)],
 'Ross and Ireland - South': [('Ross and Bizzell - South', 2)],
 'Ross and Bizzell - South': [('Wisenbaker - East', 3)],
 'Wisenbaker - East': [('The Gardens', 7)],
 'The Gardens': [('Becky Gates Center', 8)],
 'Becky Gates Center': [('Hensel @ Texas', 2)],
 'Hensel @ Texas': [('Zachry', 2)],
 'Zachry': [('Ross and Bizzell - North', 1)],
 'Reed Arena/Lot 97': [('Ag Building', 7)],
 'Ag Building': [('GGB', 9)],
 'GGB': [('Bush School', 7)],
 'Bush School': [('GERB', 9)],
 'GERB': [('Lot 108/UPD', 1)],
 'Lot 108/UPD': [('Technology Loop', 1)],
 'Technology Loop': [('Lot 41/43', 2)],
 'Lot 41/43': [('Bush School 0 Inbound', 8)],
 'Bush School 0 Inbound': [('GGB', 8)],
 'Ag Building - Inbound': [('Reed Arena', 10)],
 'Vet School': [('Transit', 3)],
 'Transit': [('Facilities Services', 1)],
 'Facilities Services': [('GSC', 1)],
 'GSC': [('Facilities Services - Inbound', 1)],
 'Facilities Services - Inbound': [('Transit - Inbound', 2)],
 'Transit - Inbound': [('Lot 71', 1)],
 'Lot 71': [('Vet School - Inbound', 3)],
 'Vet School - Inbound': [('Wehner - Inbound', 6)],
 'MSC Bus Stop': [('A.P. Beutel Health Center', 9)],
 'A.P. Beutel Health Center': [('Kleberg Center', 6)],
 'Kleberg Center': [('420 John Kimbrough Blvd', 1)],
 '420 John Kimbrough Blvd': [('Texas A&M University', 9)],
 'Texas A&M University': [('503 George Bush Dr W', 10)],
 '503 George Bush Dr W': [('Park West', 9)],
 'Park West': [('Olsen Field @ Blue Bell Park', 6)],
 'Olsen Field @ Blue Bell Park' : [('Rec Center', 2)],
 
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


start = "Commons"
end = "Transit - Inbound"

came_from, cost_so_far = a_star_search(busGraph, start, end)
print(reconstruct_path(came_from, start, end))
print('total time: ', cost_so_far[end])


        
    
    