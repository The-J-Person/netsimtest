###
# simpleBP.py
# Simple-Bisection Pruning Algorithm
###

import numpy as np
from siminit import link,node,djikstra,cost, enable_all_links

def simple_bisection_pruning(nodes,links,source,target, constraint, search_count):
    saved_route = None
    route = djikstra(nodes,links,source,target)
    if route != None and len(route) <= constraint:
        search = search_count
        saved_route = route
        path_concave_cost = cost(route)
        L = 0
        U = 1
    else:
        search = 0
    while search != 0:
        epsilon = (L+U) / 2
        for link in links:
            if link.get_cost() >= epsilon * path_concave_cost:
                link.set_enabled(False)
        route = djikstra(nodes,links,source,target)
        if route != None and len(route) <= constraint:
            saved_route = route
            path_concave_cost = cost(route)
            U = (L+U) / 2
        else:
            L = (L+U) / 2
        enable_all_links(links)
        search -= 1
    return saved_route