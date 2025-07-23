# LP_Refinery_Optimization
This repository contains the formulation of an optimization problem regarding a refinery facility. 

# Description
The basic idea is to determine the feeds of the process in order to maximize utility based of the
market price of the final productos and the costs of the feeds. As refinery processes are so big in
their size, a good approach is to linearize the problem for its optimization using historical data.

Other solutions have been proposed for this problem, differences focusing specially in the modeling
of the divisors and the level of generalization of the process. My approach is trying
to get the level of detail neccesary for get a solution that won't need further clarification or
wrangling, having the closest mathematical modelation posible for the actual process and mantaining
a linear programming, but at the same time being general enough that it will allow to add units, current
or components without having to go through significant changes.

# Future work
At the moment, it is getting a optimal solution with feasibility problems in three constrains. These
contrains being the ones regarding the first group of divisors that process multiple components. 
These divisor are behaving like destilations towers followed by divisors. This could be easily be
solved by using a non-linear approach. But I believe that a solution using binary variables is possible.






