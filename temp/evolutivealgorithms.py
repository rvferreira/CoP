import sys

from utils import population_evolve, population_mutate, population_init
from fitness import ackley, rastrigin, rosenbrock


#simulation parameters
REPRESENTATION = 'REAL'
CROSSOVER = 'MEAN'
MUTATION_RATE = 0.3
MUTATION_EFFECT_MODE = 'PLUS_MINUS'
MUTATION_EFFECT_INTENSITY = 0.2
PARENTS_SELECTION = 'ROULETTE'
INITIAL_POPULATION_SIZE = 1000
INITIAL_POPULATION_MODE = 'RANDOM'
INDIVIDUAL_DIMENSIONS_COUNT = 4
LAST_GENERATION = 40

def test_fitness(population_vector, fitness_vector, fitness_function, population_size):
	for i in range(population_size):
		fitness_vector[i] = fitness_function(population_vector[i])
		if fitness_vector[i] == 0.0:
			return i

	return -1


def main():
	population = []
	fitness = []
	results_by_generation = []

	population_init(population, fitness, INITIAL_POPULATION_SIZE, INDIVIDUAL_DIMENSIONS_COUNT)
	
	for i in range(LAST_GENERATION):

		print 'GENERATION:', i
		zero_fitness_element = test_fitness(population, fitness, rosenbrock, INITIAL_POPULATION_SIZE)
		if zero_fitness_element != -1:
			print "\nOptimal fitness was found at element", zero_fitness_element
			print population[zero_fitness_element]
			break

		best_fitness_element = fitness.index(min(fitness))
		print "Best fitness for this generation was found to be", fitness[best_fitness_element], "at the element", best_fitness_element
		print population[best_fitness_element]
		print '\n'

		results_by_generation.append(fitness[best_fitness_element])

		population = population_evolve(population, fitness, INITIAL_POPULATION_SIZE, CROSSOVER)
		population_mutate(population, MUTATION_RATE, MUTATION_EFFECT_MODE, MUTATION_EFFECT_INTENSITY)


	if zero_fitness_element == -1:
		best_fitness_element = fitness.index(min(fitness))
		print "Best fitness was found to be", fitness[best_fitness_element], "at the element", best_fitness_element
		print population[best_fitness_element]


if __name__ == '__main__': main()
