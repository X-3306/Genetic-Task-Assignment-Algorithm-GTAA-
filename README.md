# Genetic-Task-Assignment-Algorithm-GTAA

This code is an implementation of a genetic algorithm to solve an optimization problem. The problem involves assigning people to tasks based on a set of attributes or characteristics. The code defines the problem parameters, including the tasks, people, and attributes for each task-person pair. It then initializes a population of individuals, where each individual represents an assignment of people to tasks. The genetic algorithm iteratively evolves the population over a fixed number of generations. In each generation, it applies selection, crossover, and mutation operations to create a new population. The fitness function calculates the fitness of each individual, which is a measure of how well the assignment satisfies the problem constraints. Finally, the code outputs the best individual found by the algorithm and its corresponding fitness value.


# Objective function: 
$\sum_{i=1}^n\sum_{j=1}^m v_{ij}x_{ij}$, where $v_{ij}$ is the value at position $i,j$ in the vector $v$, and $x_{ij}$ is the value at position $i,j$ in the genotype vector.

# Selection: 
applying the fitness function $f(x)$ to each individual $x$, and then selecting the $k$ best individuals based on the value of $f(x)$.

# Crossover: 
selecting a crossover point $p$ and exchanging fragments of the genotypes between two parents to produce two offspring.

# Mutation: 
randomly changing the value of one or more genes in one individual.
