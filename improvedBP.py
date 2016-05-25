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

def improved_bisection_pruning(nnodes,nlinks,source,target):
    newlen = 'R'
    oldlen = 'R'
    search = 1
    TemporaryE = source
    SavedRoute = None
    nodes = nnodes.clone()
    links = nlinks.clone()
    while search!=0:
        route = djikstra(nodes, links, source, target)
        if route is not None and len(route)<=L:
            oldlen=newlen
            SavedRoute = route
            PathConcaveCost = cost(route)
            for link in <node>.links(): #What do I even put here
                if cost(route)>=epsilon*PathConcaveCost :
                    route.remove(link)
                    newlen=PruningFactor*PathConcaveCost;
        else :
            for link in <node>.links():
                if li.cost>=(newlen+oldlen)/2:
                    route.remove(link)
            newlen=(newlen+oldlen)/2
            NumberOfFail -= 1
            if NumberOfFail == 0 :
                search = 0            
    return SavedRoute