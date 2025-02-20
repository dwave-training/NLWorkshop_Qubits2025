# NL Solver Workshop (Qubits 2025)
# Problem Statement
Now that we've looked at a simple problem, let's code up a solution to the Knapsack Problem (KP).

As explained in the slideshow, the KP is a simple archetype of optimization problems where you have a container (such as a knapsack) and a set of items.

* The container has a maximum weight capacity $C$.
* Every item $k$ has a value $v_k$ and a weight $w_k$. 
* We will also include a capacity $M$ on the number of items that can be held


FIX INSERT IMAGE.
The *objective* is to pack as much value into the bag as you can. You are *constrained* by the weight capacity of the container and how many items can fit. The *decisions* you have to make are which items to bring and which to leave behind. There are multiple ways to solve this problem with D-Wave's NL hybrid solver, but one is far superior. Can you think of principles we used while exploring the Traveling Salesperson Problem that might make your model more efficient?

## Setup
To get access to our solvers, give your non-gmail email address to a D-Wave representative at the workshop. They will then be able to give you access and you will receive an acceptance email. Follow the email to create your D-Wave Leap™ cloud platform account. Then return to this repository. Open up Codespaces by clicking on the ![alt text](resources/button.png) button and selecting ![alt text](resources/button2.png). You will be asked to enter the following code into the Codespaces terminal:

`dwave setup --oob`

which will link you back to the Leap website for authentication. Copy the authorization code and paste it into the prompt on your Codespaces terminal. After that, you can open our template file FIX INSERT FILE NAME and begin coding your solution!

## Caveat
Although the KP is a fantastic example for teaching, D-Wave's quantum and hybrid solvers would be unable to provide an advantage over classical tools if we only look at the unaltered archetypal problem. This is because the problem is entirely linear!
FIX KEEP? IT HINTS THAT THE PROBLEM IS LINEAR WHICH MIGHT HELP THEM TOO MUCH.