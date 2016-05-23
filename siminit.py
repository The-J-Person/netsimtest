###
# siminit.py
# Initiates a graph for one run of the simulation
###

import random
from math import sqrt

###
# Instructions:
# Create a grid sized rect_x by rect_y
# Randomly select nodes_amount cells on the grid as "occupied".
# For each occupied cell create a node object.
# For each node, add a connection to any node that is within link_dist distance 
# (between their corresponding cells, use pythagoras to measure distance, link weight is 1 regardless of distance).
# Place all nodes in a list and return the list.
# NOTE: You may have to create your own node class as the ones available online do not appear appropriate for the task.
###

class link:
    """Essentially a stand in for a cost-target tuple"""
    def __init__(self,source,cost,target):
        self.source = source
        self.cost = cost
        self.target = target
    def get_source(self):
        return self.source
    def get_cost(self):
        return self.cost
    def get_target(self):
        return self.target
    def get_contents(self):
        return self.source, self.cost, self.target

class node:
    """Defines a network node"""
    def __init__(self, loc_x,loc_y):
        self.x = loc_x
        self.y = loc_y
        self.neighbors = []
    #===========================================================================
    # def add_neighbor(self, cost, target):
    #     self.neighbors.append(link(cost,target))
    #===========================================================================
    def add_link(self, li):
        self.neighbors.append(li)
    def get_links(self):
        return self.neighbors
    def coordinates(self):
        return self.x , self.y
    
def djikstra(nodes,links,source,dest):
    route = []
    #do things
    return route

def cost(route):
    totcost = 0
    for li in route:
        totcost += li.get_cost()
    return totcost

def Initialite_Random_Graph(rect_x=800,rect_y=800,nodes_amount=420,link_dist=75):
    graph = [[None]*rect_x]*rect_y
    nodes = []
    links = []
    random.seed()
    for _ in range(nodes_amount):
        fine = False
        while not fine:
            x = random.randrange(rect_x)
            y = random.randrange(rect_y)
            if graph[y][x] is None:
                fine = True
        near_nodes=[]    
        for N in nodes:
            xo, yo = N.coordinates()
            xd = abs(x-xo)
            yd = abs(y-yo)
            # dist^2 == xd^2 + yd^2
            if link_dist**2>=xd**2+yd**2:
                near_nodes.append(N)
        graph[y][x] = node(x,y)
        nodes.append(graph[y][x])
        for N in near_nodes:
            xo, yo = N.coordinates()
            xd = abs(x-xo)
            yd = abs(y-yo)
            li = link(N,sqrt(xd**2+yd**2),graph[y][x])
            N.add_link(li)
            ln = link(graph[y][x],sqrt(xd**2+yd**2),N)
            graph[y][x].add_link(ln)
            links.append(li)
            links.append(ln)
    return nodes, links