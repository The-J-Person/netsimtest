###
# netsimtest.py
# Runs simulation based 
###

###
# Instructions:
# Each simulation consists of initiating a random graph and one of the two algorithms times.
# For each initialization, select a number* of node pairs (source&target),
# and the variable H_max.
#     "For each routing case, a constraint on the number on the number of hops must be satisfied...
#      This constraint constraint is selected randomly from the range [10,H_max]."
# * The number of nodes selected and the nodes themselves are to be based on the uniform distribution.
# 
# Record number of successes. Record average number of hops (for successes ONLY)
# Record Success Ratio ( = Number of Tries/Number of Successes )
# Record Overall Performance ( = 75*(Success Ratio/Average Cost) )
###

import simpleBP,improvedBP,siminit

