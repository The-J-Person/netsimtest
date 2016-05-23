###
# improvedBP.py
# Improved-Bisection Pruning Algorithm
###

from siminit import link,node,djikstra,cost

###
# Instructions:
# Implement Improved-Bisection Pruning Algorithm
# (Page 4, bottom box)
###


#
# IDENTIFY THIS
L = 75.0
#
#

def improved_bisection_pruning(nodes,links,source,target):
    newlen = 'R'
    oldlen = 'R'
    search = 1
    TemporaryE = 'E'
    SavedRoute = None
    while search!=0:
        route = djikstra(nodes, links, source, target)
        if route is not None and len(route)<=L:
            oldlen=newlen
            SavedRoute = route
            PathConcaveCost = cost(route)
            
            
    return SavedRoute