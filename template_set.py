# Copyright 2025 D-Wave
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## ------- import packages and instantiate sampler -------

'''
Import the relevant packages here.
'''
from dwave.optimization import Model
from dwave.system import LeapHybridNLSampler

'''
Define sampler here
'''
sampler = LeapHybridNLSampler()


## ------- Functions

def create_model(weights,values,weight_capacity,num_capacity):
    '''
    Create the model and return it.
    '''

    ## First create an empty model object
    model = Model()
    ## Then define your variable(s) and constant(s)
    x = model.set(len(weights),max_size=num_capacity)
    v = model.constant(values)
    w = model.constant(weights)
    wc = model.constant(weight_capacity)
    ## Now create your objective function
    model.minimize(-v[x].sum())
    ## Add in constraints
    model.add_constraint(w[x].sum() <= wc)
    ## Return the model object
    return model

def run_sampler(model,time_limit = 5):
    '''
    Run the sampler and return the objective value of your solution.
    '''
    sampler.sample(model)
    with model.lock():
        best_value = model.objective.state(0)
    return best_value
    


def basic_test():
    '''
    A function which makes sure your model is correct by testing an obvious problem easily solved by hand.
    '''
    weights = [1,1,1] #  Weights of objects to put in the knapsack
    values = [10,15,20] # Values of the objects to put in the knapsack
    weight_capacity = 50 # How much weight the knapsack can hold
    num_capacity = 2 # How many objects the knapsack can hold
    easy_model = create_model(weights, values, weight_capacity, num_capacity) # Run your model-defining function
    best_value = run_sampler(easy_model) # Run the sampling function
    # Testing to make sure you got the best answer!
    if best_value == -35.0:
        print('\nCorrect answer for basic test.')
        return(True)
    else:
        print('\nIncorrect answer for the basic test!')
        return(False)

def scaling_test():
    '''
    A function which tests to make sure the number of nodes in your model scales well as problem size increases.
    '''
    node_count = []
    for k in range(5,12):
        test_model = create_model(range(k), range(k), k*100, 2) # Create a model for a knapsack problem with k items
        node_count.append(test_model.num_nodes()) # Read off how many nodes are in your model
    if len(set(node_count)) > 1: # If the number of nodes changes at all...
        print('Your model scales poorly.') # ... then the model isn't as efficient as it could be!
        return(False)
    else:
        print('Your model scales well with the node count.')
        return(True)

continue_on = basic_test()
if continue_on:
    continue_on_again = scaling_test()
    if continue_on_again:
        print('Success! Your model scales well and is very efficient.\n')





