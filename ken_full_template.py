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

from dwave.optimization.model import Model
from dwave.system import LeapHybridNLSampler

'''
Define sampler here
'''
sampler = LeapHybridNLSampler()

## ------- Functions

def create_model(weights,values,weight_capacity,num_capacity):
    num_items = len(weights)


    ## First create an empty model object
    model = Model()
    ## Then define your variable(s) and constant(s)
    vars = model.set(num_items,max_size=num_capacity)
    weights = model.constant(weights)
    values = model.constant(values)
    weight_capacity = model.constant(weight_capacity)
    ## Now create your objective function
    model.minimize(-values[vars].sum())

    ## Add in constraints and you're done!
    model.add_constraint(weights[vars].sum() <= weight_capacity)

    ## Return the model objective
    return model

def run_sampler(model,time_limit = 5):
    ## Run the sampler and return the the solution as [sampleset, objective value]
    sampler.sample(model,time_limit=5)
    with model.lock():
        sampleset = list(sym.state(0) for sym in model.iter_decisions())
        best_value = model.objective.state(0)
    return sampleset,best_value
    


def basic_test():
    # First Test
    ## Should be obvious solution easily done by hand
    weights = [1,1,1]
    values = [10,15,20]
    weight_capacity = 50
    num_capacity = 2
    easy_model = create_model(weights, values, weight_capacity, num_capacity)
    sampleset, best_value = run_sampler(easy_model)
    if best_value == -35.0:
        print('Correct answer for basic test.\n')
        return(True)
    else:
        print('Incorrect answer for the basic test!\n')
        return(False)

def scaling_test():
    node_count = []
    for k in range(5,12):
        test_model = create_model(range(k), range(k), k*100, 2)
        node_count.append(test_model.num_nodes())
    if len(set(node_count)) > 1:
        print('Your model scales poorly.\n')
        return(False)
    else:
        print('Your model scales well with the node count.\n')
        return(True)

continue_on = basic_test()
if continue_on:
    continue_on_again = scaling_test()
    if continue_on_again:
        print('Success! Your model scales well and is very efficient.')





