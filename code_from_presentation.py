from dwave.optimization import Model
import numpy as np
from dwave.system import LeapHybridNLSampler
model = Model()
matrix = np.array([
		[0, 3, 9, 5, 1],
		[3, 0, 2, 6, 4],
		[9, 2, 0, 7, 8],
		[5, 6, 7, 0, 2],
		[1, 4, 8, 2, 0],
		])
D = model.constant(matrix)
x = model.list(5)
model.minimize((D[x[:-1], x[1:]]).sum()+ (D[x[-1], x[0]]))
sampler = LeapHybridNLSampler() 

# Sample
sampler.sample(model, label='NL Example - TSP')


# Test the initial state
with model.lock():
	model.states.resize(1)
	x.set_state(0,[0,2,4,3,1])
	#x.set_state(0,[0,4,2,3,1])
	print(f"For state 0, x = {x.state(0)} results in an objective value of {model.objective.state(0)}")

"""

# Read best samples
with model.lock():
	current_state = 0
	print(f"For state {current_state}, x = {x.state(current_state)} results in an objective value of {model.objective.state(current_state)}")
"""
