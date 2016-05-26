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
    
    options = ("total_costs","total_hops","success_count","fail_count")
    dict_simple = {}
    for i in range(5,31):
        dict_simple[i] = {}
        for j in options:
            dict_simple[i][j] = 0
    dict_improved = {}
    for i in range(5,31):
        dict_improved[i] = {}
        for j in options:
            dict_simple[i][j] = 0
    
        

    
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
    for i in range(5,31):
        avg_imp_dict[i] = [0,0]
    
     
     
    
    for x in range(number_of_iteration):
        node, links = siminit.Initialite_Random_Graph()
        source = randomal(node)
        target = randomal(node)
        while target == source:
            target = randomal(node)
               
        hops = max_hops()
        
        route_simple = simpleBP.simple_bisection_pruning(node , links, node[source], node[target],hops, search_count )
        route_improved = improvedBP.improved_bisection_pruning(node , links , node[source], node[target],hops)
        
        print(dict_simple)
        
        if(route_simple != None):
            dict_simple[hops]["total_costs"] += siminit.cost(route_simple)
            dict_simple[hops]["total_hops"] += len(route_simple)
            dict_simple[hops]["success_count"] += 1
        else:
            dict_simple[hops]["fail_count"] += 1
        
        print(dict_improved)
        
        if(route_improved != None):
            dict_improved[hops]["total_costs"] += siminit.cost(route_improved)
            dict_improved[hops]["total_hops"] += len(route_improved)
            dict_improved[hops]["success_count"] += 1
        else:
            dict_improved[hops]["fail_count"] += 1
        
        """ OFIR EDITED UNTIL HERE"""
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

    ### J started editing here ###
    scale = []
    avg_costs = []
    succ_rate = []
    avg_hops = []
    ovr_perf = []
    avg_costsi = []
    succ_ratei = []
    avg_hopsi = []
    ovr_perfi = []
    for i in range(5,31):
        scale.append(i)
        avg_costs.append(dict_simple[i]["total_costs"] / dict_simple[i]["success_count"])
        succ_rate.append(dict_simple[10]["success count"] / (  dict_simple[10]["success_count"] +  dict_simple[10]["fail_count"] ))
        avg_hops.append(dict_simple[10]["total_hops"] /  dict_simple[10]["success_count"])
        ovr_perf.append(succ_rate[i-5]/avg_costs[i-5])*75
        avg_costsi.append(dict_improved[i]["total_costs"] / dict_improved[i]["success_count"])
        succ_ratei.append(dict_improved[10]["success count"] / (  dict_improved[10]["success_count"] +  dict_improved[10]["fail_count"] ))
        avg_hopsi.append(dict_improved[10]["total_hops"] /  dict_improved[10]["success_count"])
        ovr_perfi.append(succ_ratei[i-5]/avg_costsi[i-5])*75
        
    plt.plot(scale,succ_rate, color = 'r')
    plt.plot(scale,succ_ratei, color = 'g')
    plt.xlabel("Max Hop")
    plt.ylabel("Success Ratio")
    plt.show()
    
    plt.plot(scale,avg_costs, color = 'r')
    plt.plot(scale,avg_costsi, color = 'g')
    plt.xlabel("Max Hop")
    plt.ylabel("Average Longest Link")
    plt.show()
    
    plt.plot(scale,avg_hops, color = 'r')
    plt.plot(scale,avg_hopsi, color = 'g')
    plt.xlabel("Max Hop")
    plt.ylabel("Average Hop Count")
    plt.show()
    
    plt.plot(scale,ovr_perf, color = 'r')
    plt.plot(scale,ovr_perfi, color = 'g')
    plt.xlabel("Max Hop")
    plt.ylabel("Overall Performance")
    plt.show()
    ### J stopped editing here ###
    
     
def randomal(nodes):
    return random.randrange(0 , len(nodes))

def max_hops():
    return random.randrange(5 , 31)



simulation_process(count, 35)
     