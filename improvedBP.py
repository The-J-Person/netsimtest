###
# improvedBP.py
# Improved-Bisection Pruning Algorithm
###

from siminit import link,djikstra,cost, enable_all_links

"""
missing information: epsilon value (pruning factor) & fails_allowed, will comlete that on our own
"""
def improved_bisection_pruning(nodes,links,source,target, constraint, fails_allowed = 3, R = 75, epsilon = 0.75):
    newlen = R
    oldlen = R
    search = 1
    saved_route = None
    while search != 0:
        route = djikstra(nodes, links, source, target)
        if route != None and len(route) <= constraint:
            oldlen=newlen
            saved_route = route
            path_concave_cost = cost(route)
            for link in links:
                if link.get_cost() >= epsilon*path_concave_cost:
                    link.set_enabled(False)
            newlen = epsilon * path_concave_cost;
        else:
            enable_all_links(links)
            for link in links:
                if link.get_cost() >= (newlen+oldlen)/2:
                    link.set_enabled(False)
            newlen=(newlen+oldlen)/2
            fails_allowed -= 1
            if fails_allowed == 0 :
                search = 0            
    return saved_route