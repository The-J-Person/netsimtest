###
# siminit.py
# Initiates a graph for one run of the simulation
###

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

def Initialite_Random_Graph(rect_x=800,rect_y=800,nodes_amount=420,link_dist=75):
    graph = False # Placeholder, this obviously needs to be replaced
    return graph