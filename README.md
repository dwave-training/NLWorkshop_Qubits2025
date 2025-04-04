# NL Solver Workshop (Qubits 2025)
# Problem Statement
Now that we've looked at the Traveling Salesperson (TSP) problem, let's code up a solution to the Knapsack Problem (KP).

As explained in the slideshow, the KP is an optimization problem where you have a container (such as a knapsack) and a set of items.

* A collection of objects is to be shipped, where every item $k$ has a value $v_k$ and a weight $w_k$. 
* The total weight of the shipped container has a maximum weight capacity $C$.
* The container can hold at most $M$ items.



<img src=resources/knapsack.png width="600">

The *objective* is to maximize the total value of the knapsack bag. You are *constrained* by the weight capacity of the container and how many items can fit in it. The *decisions* you have to make are which items to bring and which to leave behind. There are multiple ways to solve this problem with D-Wave's NL hybrid solver, but one is far superior. Can you think of principles we used while exploring the NL solver in the Traveling Salesperson Problem? What choice of symbols will make your model more efficient?

## Setup
Having signed up for this workshop, a D-Wave employee has already added you to the project. You should have received an email from D-Wave notifications with a subject line similar to “You’ve been invited to a project in Leap.” Within that email is a link to accept the project invitation. Follow the invitation's instructions to create your D-Wave Leap™ cloud platform account, then return to this repository. Open up Codespaces by clicking on the ![alt text](resources/button.png) button and selecting ![alt text](resources/button2.png). You will be asked to enter the following code into the Codespaces terminal:

`dwave setup --oob`

which will link you back to the Leap website for authentication. Copy the authorization code and paste it into the prompt on your Codespaces terminal. After that, you can start coding! We've put together two templates (`template_binary.py` and `template_set.py`) with slightly different test functions at the end. With the binary template, try solving this problem with binary variables. However, using set variables will let you take more advantage of the NL solver's power.

## Note
Although the KP is a fantastic example for teaching, D-Wave's quantum and hybrid solvers would likely be unable to provide an advantage over classical tools if we only look at the classic form of the problem. This is because the problem is entirely linear!
