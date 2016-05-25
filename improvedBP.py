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
"""
missing information: epsilon value (pruning factor) 
"""
def improved_bisection_pruning(nodes,org_links,source,target, constraint, fails_allowed = 3, R = 75, epsilon = 0.75):
    newlen = R
    oldlen = R
    search = 1
    links = org_links.copy()
    temporaryE = links.copy()
    saved_route = None
    while search != 0:
        route = djikstra(nodes, links, source, target)
        if route != None and len(route) <= L:
            oldlen=newlen
            saved_route = route
            path_concave_cost = cost(route)
            for link in links():
                if cost(route) >= epsilon*path_concave_cost:
                    links.remove(link)
            newlen = epsilon * path_concave_cost;
        else:
            links = temporaryE.copy()
            for link in links():
                if link.cost >= (newlen+oldlen)/2:
                    links.remove(link)
            newlen=(newlen+oldlen)/2
            fails_allowed -= 1
            if fails_allowed == 0 :
                search = 0            
    return saved_route