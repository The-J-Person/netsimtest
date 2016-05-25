###
# netsimtest.py
# Runs simulation based 
###

##
#  Instructions:
#  Each simulation consists of initiating a random graph and one of the two algorithms times.
#  For each initialization, select a number* of node pairs (source&target),
#  and the variable H_max.
#      "For each routing case, a constraint on the number on the number of hops must be satisfied...
#       This constraint constraint is selected randomly from the range [10,H_max]."
#  * The number of nodes selected and the nodes themselves are to be based on the uniform distribution.
#  
#  Record number of successes. Record average number of hops (for successes ONLY)
#  Record Success Ratio ( = Number of Tries/Number of Successes )
#  Record Overall Performance ( = 75*(Success Ratio/Average Cost) )
##

import simpleBP,improvedBP,siminit
import random
import matplotlib.pyplot as plt

# import plotly.plotly as py
# import plotly.graph_objs as go

random.seed()
count = 3


def simulation_process(search_count, number_of_iteration):
    
    simple_b_pruning = None
    improved_b_pruning =None
    sum_sim = 0
    sum_imp = 0
    avr_sim = 0
    avr_imp = 0
    fail_sim = 0
    fail_imp = 0
    fail_avr_sim = 0
    avg_sim_dict = {}
    avg_imp_dict = {}
    max_hop = []
    avg_hop = []
    max_imp_hop = []
    avg_imp_hop = []
    for i in range(5,31):
        avg_sim_dict[i] = [0,0]
    
     
     
    
    for x in range(number_of_iteration):
        node, links = siminit.Initialite_Random_Graph()
        source = randomal(node)
        target = randomal(node)
        while target == source:
            target = randomal(node)
        
        hops = max_hops()
#         print(node)
#         simple_b_pruning = simpleBP.simple_bisection_pruning(node , links, node[source], node[target],hops, search_count )
        improved_b_pruning = improvedBP.improved_bisection_pruning(node , links , node[source], node[target],hops)
#         print(simple_b_pruning)
#         if(simple_b_pruning != None):
#             avg_sim_dict[hops][0] += siminit.cost(simple_b_pruning)
#             avg_sim_dict[hops][1] += 1
#         else:
#             fail_sim += 1
#         sum_imp += siminit.cost(improved_b_pruning)
        if(improved_b_pruning != None):
            avg_imp_dict[hops][0] += siminit.cost(improved_b_pruning)
            avg_imp_dict[hops][1] += 1
        else:
            fail_imp += 1
        print("finished a round")
            
    for i in avg_imp_dict:
        print (i)
        
#     for i in range(5,31):
#         if(avg_sim_dict[i][1] > 0):
#             test_sim_avg = avg_sim_dict[i][0] / avg_sim_dict[i][1]
#             avg_hop.append(test_sim_avg)
#             max_hop.append(i)
#             print("Max Hops = " , i , "Average" , test_sim_avg , "Count",avg_sim_dict[i][1])
#             
#     for i in range(5,31):
#         if(avg_imp_dict[i][1] > 0):
#             test_imp_avg = avg_imp_dict[i][0] / avg_imp_dict[i][1]
#             avg_imp_hop.append(test_imp_avg)
#             max_imp_hop.append(i)
#             print("Max Hops = " , i , "Average" , test_imp_avg , "Count",avg_imp_dict[i][1])
            
#     
#     for i in range(5,30):
#         if(avg_sim_dict[i][1] > 0):
#             max_hop.append(i)
#             avg_hop.append(avg_sim_dict[i][0])
#     print(max_hop)
#     print(avg_hop)
#     
#     plt.plot(max_hop, avg_hop , color = 'r')
# #     plt.plot(max_imp_hop,avg_imp_dict)
#     plt.axis([5, 31, 0, 80])
#     plt.show()         
#     trace0 = go.Scatter(
#     x = max_hop,
#     y = avg_hop,
#     name = 'Simple',
#     line = dict(
#         color = ('rgb(205, 12, 24)'),
#         width = 4))
#     
#     layout = dict(title = 'Average cost when max H is changing',
#               xaxis = dict(title = 'Max-Hop'),
#               yaxis = dict(title = 'Avg Longest Link'),
#               )
# 
# # Plot and embed in ipython notebook!
#     fig = dict(data=data, layout=layout)
#     py.iplot(fig, filename='styled-line')
       
#     if(fail_sim > 0):
#         avr_sim = sum_sim / (number_of_iteration - fail_sim)
#     else:
#         avr_sim = sum_sim / number_of_iteration
#     print(avr_sim)
#     avr_imp = sum_imp / number_of_iteration
    
    
     
def randomal(nodes):
    return random.randrange(0 , len(nodes))

def max_hops():
    return random.randrange(5 , 30)



simulation_process(count, 50)
     