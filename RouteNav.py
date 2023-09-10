

from typing import Optional, Protocol, TypeVar
import collections
import heapq
import math
import pickle



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
 'Commons': [('Ross and Bizzell - Bonfire - North', 3)],
 'Ross and Bizzell - Bonfire - North': [('Ross and Ireland - Bonfire - North', 1), ('Ross and Bizzell - Bonfire - South', 1), ('Ross and Bizzell - Gig Em - South', 1), ('Ross and Bizzell - Gig Em - North', 1)],
 'Ross and Ireland - Bonfire - North': [('Asbury Water Tower - Bonfire', 1), ('Ross and Ireland - Bonfire - South', 1), ('Ross and Ireland - Gig Em - South', 1), ('Ross and Ireland - Gig Em - North', 1)],
 'Asbury Water Tower - Bonfire': [('HEEP', 4), ('Asbury Water Tower - Gig Em', 1)],
 'HEEP': [('Kleberg - Bonfire - Outbound', 1)],
 'Kleberg - Bonfire - Outbound': [('Rec Center - Bonfire', 3), ('Kleberg - Bonfire - Inbound', 1), ('Kleberg - Bush School - Outbound', 1), ('Kleberg - Bush School - Inbound', 1), ('Kleberg - Howdy - Outbound', 1), ('Kleberg - Howdy - Inbound', 1)],
 'Rec Center - Bonfire': [('Lot 100 G', 2), ('Rec Center - Howdy', 1)],
 'Lot 100 G': [('Reed Arena - Bonfire', 2)],
 'Reed Arena - Bonfire': [('Kleberg - Bonfire - Inbound', 2), ('Reed Arena - Bush School - Inbound', 1)],
 'Kleberg - Bonfire - Inbound': [('MSC - Bonfire', 2), ('Kleberg - Bonfire - Outbound', 1), ('Kleberg - Bush School - Outbound', 1), ('Kleberg - Bush School - Inbound', 1), ('Kleberg - Howdy - Outbound', 1), ('Kleberg - Howdy - Inbound', 1)],
 'MSC - Bonfire': [('Fish Pond - Bonfire', 2), ('MSC - Yell Practice', 1), ('MSC - Bush School', 1), ('MSC - 12th Man', 1), ('MSC - Howdy', 1)],
 'Fish Pond - Bonfire': [('Ross and Ireland - Bonfire - South', 2), ('Fish Pond - Gig Em', 1)],
 'Ross and Ireland - Bonfire - South': [('Ross and Bizzell - Bonfire - South', 2), ('Ross and Ireland - Bonfire - North', 1), ('Ross and Ireland - Gig Em - South', 1), ('Ross and Ireland - Gig Em - North', 1)],
 'Ross and Bizzell - Bonfire - South': [('Southside Rec Center', 5), ('Ross and Bizzell - Bonfire - North', 1), ('Ross and Bizzell - Gig Em - South', 1), ('Ross and Bizzell - Gig Em - North', 1)],
 'Southside Rec Center': [('Lewis Street', 2)],
 'Lewis Street': [('Commons', 2)],
 'MSC - Yell Practice': [('Beutel - Yell Practice', 3), ('MSC - Bonfire', 1), ('MSC - Bush School', 1), ('MSC - 12th Man', 1), ('MSC - Howdy', 1)],
 'Beutel - Yell Practice': [('Wehner - Yell Practice - Outbound', 3), ('Beutel - 12th Man', 1), ('Beutel - Howdy', 1)],
 'Wehner - Yell Practice - Outbound': [('School of Public Health - Outbound', 8), ('Wehner - Yell Practice - Inbound', 1), ('Wehner - 12th Man - Outbound', 1), ('Wehner - 12th Man - Inbound', 1)],
 'School of Public Health - Outbound': [('White Creek 1', 2), ('School of Public Health - Inbound', 1)],
 'White Creek 1': [('White Creek 2', 1)],
 'White Creek 2': [('Lot 101', 1)],
 'Lot 101': [('NCTM', 3)],
 'NCTM': [('VTED', 2)],
 'VTED': [('Houston Building', 1)],
 'Houston Building': [('White Creek Community Center', 1)],
 'White Creek Community Center': [('School of Public Health - Inbound', 1)],
 'School of Public Health - Inbound': [('Wehner - Yell Practice - Inbound', 6), ('School of Public Health - Outbound', 1)],
 'Wehner - Yell Practice - Inbound': [('MSC - Yell Practice', 5), ('Wehner - Yell Practice - Outbound', 1), ('Wehner - 12th Man - Outbound', 1), ('Wehner - 12th Man - Inbound', 1)],
 'Asbury Water Tower - Gig Em': [('Fish Pond - Gig Em', 4), ('Asbury Water Tower - Bonfire', 1)],
 'Fish Pond - Gig Em': [('Ross and Ireland - Gig Em - South', 2), ('Fish Pond - Bonfire', 1)],
 'Ross and Ireland - Gig Em - South': [('Ross and Bizzell - Gig Em - South', 2), ('Ross and Ireland - Bonfire - South', 1), ('Ross and Ireland - Bonfire - North', 1), ('Ross and Ireland - Gig Em - North', 1)],
 'Ross and Bizzell - Gig Em - South': [('Wisenbaker - East', 3), ('Ross and Bizzell - Bonfire - South', 1), ('Ross and Bizzell - Bonfire - North', 1), ('Ross and Bizzell - Gig Em - North', 1)],
 'Wisenbaker - East': [('The Gardens', 7)],
 'The Gardens': [('Becky Gates Center', 8)],
 'Becky Gates Center': [('Hensel @ Texas', 2)],
 'Hensel @ Texas': [('Zachry', 2)],
 'Zachry': [('Ross and Bizzell - Gig Em - North', 1)],
 'Ross and Bizzell - Gig Em - North': [('Ross and Ireland - Gig Em - North', 1), ('Ross and Bizzell - Bonfire - South', 1), ('Ross and Bizzell - Gig Em - South', 1), ('Ross and Bizzell - Bonfire - North', 1)],
 'Ross and Ireland - Gig Em - North': [('Asbury Water Tower - Gig Em', 1), ('Ross and Ireland - Bonfire - South', 1), ('Ross and Ireland - Gig Em - South', 1), ('Ross and Ireland - Bonfire - North', 1)],
 'MSC - Bush School': [('Kleberg - Bush School - Outbound', 4), ('MSC - Yell Practice', 1), ('MSC - Bonfire', 1), ('MSC - 12th Man', 1), ('MSC - Howdy', 1)],
 'Kleberg - Bush School - Outbound': [('Reed Arena/Lot 97 - Bush School', 2), ('Kleberg - Bonfire - Inbound', 1), ('Kleberg - Bonfire - Outbound', 1), ('Kleberg - Bush School - Inbound', 1), ('Kleberg - Howdy - Outbound', 1), ('Kleberg - Howdy - Inbound', 1)],
 'Reed Arena/Lot 97 - Bush School': [('Ag Building - Outbound', 7), ('Reed Arena/Lot 97 - Howdy', 1)],
 'Ag Building - Outbound': [('GGB - Outbound', 9), ('Ag Building - Inbound', 1)],
 'GGB - Outbound': [('Bush School - Outbound  ', 7)],
 'Bush School - Outbound  ': [('GERB', 9)],
 'GERB': [('Lot 108/UPD', 1)],
 'Lot 108/UPD': [('Technology Loop', 1)],
 'Technology Loop': [('Lot 41/43', 2)],
 'Lot 41/43': [('Bush School - Inbound', 8)],
 'Bush School - Inbound': [('GGB - Inbound', 8)],
 'GGB - Inbound': [('Ag Building - Inbound', 7)],
 'Ag Building - Inbound': [('Reed Arena - Bush School - Inbound', 10), ('Ag Building - Outbound', 1)],
 'Reed Arena - Bush School - Inbound': [('Kleberg - Bush School - Inbound', 2), ('Reed Arena - Bonfire', 1)],
 'Kleberg - Bush School - Inbound': [('MSC - ILCB', 2), ('Kleberg - Bonfire - Inbound', 1), ('Kleberg - Bush School - Outbound', 1), ('Kleberg - Bonfire - Outbound', 1), ('Kleberg - Howdy - Outbound', 1), ('Kleberg - Howdy - Inbound', 1)],
 'MSC - ILCB': [('MSC - Bush School', 2)],
 'MSC - 12th Man': [('Beutel - 12th Man', 3), ('MSC - Yell Practice', 1), ('MSC - Bush School', 1), ('MSC - Bonfire', 1), ('MSC - Howdy', 1)],
 'Beutel - 12th Man': [('Wehner - 12th Man - Outbound', 3), ('Beutel - Yell Practice', 1), ('Beutel - Howdy', 1)],
 'Wehner - 12th Man - Outbound': [('Vet School - Outbound', 8), ('Wehner - Yell Practice - Inbound', 1), ('Wehner - Yell Practice - Outbound', 1), ('Wehner - 12th Man - Inbound', 1)],
 'Vet School - Outbound': [('Transit - Outbound', 3), ('Vet School - Inbound', 1)],
 'Transit - Outbound': [('Facilities Services - Outbound', 1)],
 'Facilities Services - Outbound': [('GSC', 1)],
 'GSC': [('Facilities Services - Inbound', 1)],
 'Facilities Services - Inbound': [('Transit - Inbound', 2)],
 'Transit - Inbound': [('Lot 71', 1)],
 'Lot 71': [('Vet School - Inbound', 3)],
 'Vet School - Inbound': [('Wehner - Inbound', 6), ('Vet School - Outbound', 1)],
 'Wehner - 12th Man - Inbound': [('MSC - 12th Man', 5), ('Wehner - Yell Practice - Inbound', 1), ('Wehner - 12th Man - Outbound', 1), ('Wehner - Yell Practice - Outbound', 1)],
 'MSC - Howdy': [('Beutel - Howdy', 9), ('MSC - Yell Practice', 1), ('MSC - Bush School', 1), ('MSC - 12th Man', 1), ('MSC - Bonfire', 1)],
 'Beutel - Howdy': [('Kleberg - Howdy - Outbound', 6), ('Beutel - 12th Man', 1), ('Beutel - Yell Practice', 1)],
 'Kleberg - Howdy - Outbound': [('Reed Arena/Lot 97 - Howdy', 10), ('Kleberg - Bonfire - Inbound', 1), ('Kleberg - Bush School - Outbound', 1), ('Kleberg - Bush School - Inbound', 1), ('Kleberg - Bonfire - Outbound', 1), ('Kleberg - Howdy - Inbound', 1)],
 'Reed Arena/Lot 97 - Howdy': [('Physical Education', 1), ('Reed Arena/Lot 97 - Bush School', 1)],
 'Physical Education': [('Park West', 4)],
 'Park West': [('Olsen Field @ Blue Bell Park', 6)],
 'Olsen Field @ Blue Bell Park': [('Rec Center - Howdy', 3)],
 'Rec Center - Howdy': [('Kleberg - Howdy - Inbound', 3), ('Rec Center - Bonfire', 1)],
 'Kleberg - Howdy - Inbound': [('MSC - Howdy', 9), ('Kleberg - Bonfire - Inbound', 1), ('Kleberg - Bush School - Outbound', 1), ('Kleberg - Bush School - Inbound', 1), ('Kleberg - Howdy - Outbound', 1), ('Kleberg - Bonfire - Outbound', 1)]
}




def heuristic() -> float:
    return 1

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
end = 'Ag Building - Outbound'

came_from, cost_so_far = a_star_search(busGraph, start, end)
print(reconstruct_path(came_from, start, end))
print('total time: ', cost_so_far[end])


        
    
    