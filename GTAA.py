import random

# Define the problem parameters
T = ['t1', 't2', 't3', 't4']  # tasks
P = ['p1', 'p2', 'p3', 'p4', 'p5']  # people
k = 3  # number of attributes for each task-person pair

# Define the vectors for each task-person pair
vectors = {}
for t in T:
    for p in P:
        vectors[(t, p)] = [random.randint(-10, 10) for i in range(k)]

# Define the genetic algorithm parameters
population_size = 20
num_generations = 100
mutation_rate = 0.1

# Define the fitness function
def fitness(individual):
    total_fitness = 0
    for t in T:
        total_fitness += vectors[(t, individual[t])]
    return total_fitness

# Define the selection function
def selection(population):
    population_fitness = [fitness(individual) for individual in population]
    max_fitness = max(population_fitness)
    selection_probs = [fitness/sum(population_fitness) for fitness in population_fitness]
    selected_index = random.choices(range(len(population)), selection_probs)[0]
    return population[selected_index]

# Define the crossover function
def crossover(parent1, parent2):
    child = {}
    for t in T:
        if random.random() < 0.5:
            child[t] = parent1[t]
        else:
            child[t] = parent2[t]
    return child

# Define the mutation function
def mutation(individual):
    for t in T:
        if random.random() < mutation_rate:
            individual[t] = random.choice(P)
    return individual

# Initialize the population
population = [{} for i in range(population_size)]
for individual in population:
    for t in T:
        individual[t] = random.choice(P)

# Run the genetic algorithm
for i in range(num_generations):
    # Selection
    new_population = []
    for j in range(population_size):
        parent1 = selection(population)
        parent2 = selection(population)
        child = crossover(parent1, parent2)
        child = mutation(child)
        new_population.append(child)
    population = new_population

# Find the best individual
best_individual = max(population, key=fitness)

# Print the results
print('Best individual: ', best_individual)
print('Fitness: ', fitness(best_individual))
