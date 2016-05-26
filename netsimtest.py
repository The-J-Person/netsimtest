###
# netsimtest.py
# Runs simulation 
###

import simpleBP,improvedBP,siminit
import random
import matplotlib.pyplot as plt

random.seed()
count = 3

def randomal(nodes):
    return random.randrange(0 , len(nodes))

def max_hops():
    return random.randrange(5 , 31)

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
            dict_improved[i][j] = 0
            
    avg_sim_dict = {}
    avg_imp_dict = {}
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
        
        if(route_simple != None):
            dict_simple[hops]["total_costs"] += siminit.cost(route_simple)
            dict_simple[hops]["total_hops"] += len(route_simple)
            dict_simple[hops]["success_count"] += 1
        else:
            dict_simple[hops]["fail_count"] += 1
        
        if(route_improved != None):
            dict_improved[hops]["total_costs"] += siminit.cost(route_improved)
            dict_improved[hops]["total_hops"] += len(route_improved)
            dict_improved[hops]["success_count"] += 1
        else:
            dict_improved[hops]["fail_count"] += 1
        print ("finished Iteration:" , x)
        
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
        if dict_simple[i]["success_count"]>0 :
            succc=dict_simple[i]["success_count"] / (  dict_simple[i]["success_count"] +  dict_simple[i]["fail_count"] )
            avggg=dict_simple[i]["total_costs"] / dict_simple[i]["success_count"]
            avg_costs.append(avggg)
            succ_rate.append(succc)
            avg_hops.append(dict_simple[i]["total_hops"] /  dict_simple[i]["success_count"])
            ovr_perf.append((succc/avggg)*75)
        else : 
            avg_costs.append(0)
            succ_rate.append(0)
            avg_hops.append(0)
            ovr_perf.append(0)
        if dict_improved[i]["success_count"]>0 :
            succi=dict_improved[i]["success_count"] / (  dict_improved[i]["success_count"] +  dict_improved[i]["fail_count"] )
            avggi=dict_improved[i]["total_costs"] / dict_improved[i]["success_count"]
            avg_costsi.append(avggi)
            succ_ratei.append(succi)
            avg_hopsi.append(dict_improved[i]["total_hops"] /  dict_improved[i]["success_count"])
            ovr_perfi.append((succi/avggi)*75)
        else :
            avg_costsi.append(0)
            succ_ratei.append(0)
            avg_hopsi.append(0)
            ovr_perfi.append(0)
        
    plt.plot(scale,succ_rate, 'r-',label='Simple Bisection Pruning')
    plt.plot(scale,succ_ratei, 'g-',label='Improved Bisection Pruning')
    plt.xlabel("Max Hop")
    plt.ylabel("Success Ratio")
    plt.legend()
    plt.show()
    
    plt.plot(scale,avg_costs, 'r-',label='Simple Bisection Pruning')
    plt.plot(scale,avg_costsi, 'g-',label='Improved Bisection Pruning')
    plt.xlabel("Max Hop")
    plt.ylabel("Average Longest Link")
    plt.legend()
    plt.show()
    
    plt.plot(scale,avg_hops, 'r-',label='Simple Bisection Pruning')
    plt.plot(scale,avg_hopsi, 'g-',label='Improved Bisection Pruning')
    plt.xlabel("Max Hop")
    plt.ylabel("Average Hop Count")
    plt.legend()
    plt.show()
    
    plt.plot(scale,ovr_perf, 'r-',label='Simple Bisection Pruning')
    plt.plot(scale,ovr_perfi, 'g-',label='Improved Bisection Pruning')
    plt.xlabel("Max Hop")
    plt.ylabel("Overall Performance")
    plt.legend()
    plt.show()
    
    print (dict_simple)
    print (dict_improved)

simulation_process(count, 5000)