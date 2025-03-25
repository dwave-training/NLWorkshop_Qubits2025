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


'''
Define sampler here
'''


## ------- Functions

def create_model(weights,values,weight_capacity,num_capacity):
    '''
    Create the model and return it.
    '''


    ## First create an empty model object

    ## Then define your variable(s) and constant(s)

    ## Now create your objective function

    ## Add in constraints

    ## Return the model object
    return model

def run_sampler(model,time_limit = 5):
    '''
    Run the sampler and return the the solution as [sampleset, objective value]
    '''


    return sampleset,best_value
    


def basic_test():
    '''
    A function which makes sure your model is correct by testing an obvious problem easily solved by hand.
    '''
    weights = [1,1,1] #  Weights of objects to put in the knapsack
    values = [10,15,20] # Values of the objects to put in the knapsack
    weight_capacity = 50 # How much weight the knapsack can hold
    num_capacity = 2 # How many objects the knapsack can hold
    easy_model = create_model(weights, values, weight_capacity, num_capacity) # Run your model-defining function
    sampleset, best_value = run_sampler(easy_model) # Run the sampling function
    # Testing to make sure you got the best answer!
    if best_value == -35.0:
        print('Correct answer for basic test.\n')
        return(True)
    else:
        print('Incorrect answer for the basic test!\n')
        return(False)


continue_on = basic_test()
if continue_on:
    print('Congratulations! Your binary model functions well.\n Try with set variables next!')





