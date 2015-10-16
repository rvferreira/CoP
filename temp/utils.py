from random import seed, randrange
from math import cos, exp, sqrt, pi, fsum
from fitness import ackley
import operator

DECIMAL_APPROX = 6

INITIAL_FITNESS = 50.0
CROSSOVER_METHOD = 'MEAN'
POPULATION_SIZE = 400
DIMENSIONS = 4
MUTATION_MODE = 'PLUS_MINUS'
MUTATION_INTENSITY = 0.1

#individual generation parameters
MIN_X_RANGE = -5.0
MAX_X_RANGE = 5.0

class Element:

	@property
	def x():
		return self.x

	def __init__(self, n_dimensions, x_array=[]):
		seed()
		
		self.x = []
		self.fitness = INITIAL_FITNESS

		if not x_array:	
			for i in range(n_dimensions):
				(self.x).append(randrange(MIN_X_RANGE*100.0, MAX_X_RANGE*100.0) / 100.0)
		else:
			(self.x) = x_array

	def computeElementFitness(self, fitness_function):
		self.fitness = fitness_function(self.x)


class Population:
	def __init__(self, initial_population_size, n_dimensions):
		self.n_dimensions = n_dimensions
		self.elements = []

		for i in range(initial_population_size):
			self.elements.append(Element(n_dimensions))

	def computeFitness(self, fitness_function):
		for element in self.elements:
			element.computeElementFitness(fitness_function)
		(self.elements).sort(key=operator.attrgetter('fitness'))

	def parents_select(self):
		# roll that prioritizes best parents
		first_parent_roll = 0.8 ** (randrange(0, 100)/(-5.077) - 1) - 1.2
		second_parent_roll = 0.8 ** (randrange(0, 100)/(-5.077) - 1) - 1.2

		# normalizing for population size
		first_parent_roll = int((first_parent_roll / 100.0) * len(self.elements))
		second_parent_roll = int((second_parent_roll / 100.0) * len(self.elements))

		first_parent = self.elements[first_parent_roll]
		second_parent = self.elements[second_parent_roll]

		return [first_parent, second_parent]

	def crossover(self, crossover_point, crossover_method):
		parents_vector = self.parents_select()
		#print parents_vector[0].x
		#print parents_vector[1].x

		parents_merge_vector = []
		if crossover_method == 'MEAN':
			for i in range(crossover_point):
				merge_x = 0
				for p in parents_vector:
					merge_x += p.x[i] 
				merge_x /= float(len(parents_vector))
				parents_merge_vector.append(round(merge_x, DECIMAL_APPROX))

		child = Element(self.n_dimensions, parents_merge_vector[0:crossover_point] + parents_vector[0].x[crossover_point:len(parents_vector[0].x)])
		return child

	def evolve(self, fitness_function, mutation_rate):
		self.computeFitness(fitness_function)

		print "ANTES"
		for elem in self.elements:
			print elem.fitness, " ", elem.x
		print "\n"

		for i in range(len(self.elements)):
			self.elements.append(self.crossover(randrange(0, self.n_dimensions+1), CROSSOVER_METHOD))

		self.mutate(mutation_rate, MUTATION_MODE, MUTATION_INTENSITY)

		self.computeFitness(fitness_function)

		self.elements = self.elements[0:len(self.elements)/2]

		print "DESPUES"
		for elem in self.elements:
			print elem.fitness, " ", elem.x
		print "\n"

	def mutate(self, mutation_rate, mutation_mode, mutation_intensity):
		seed()

		if mutation_mode == 'PLUS_MINUS':
			for element in self.elements:
				for j in range(len(element.x)):
					chance = randrange(0, 100)/100.0
					if chance < mutation_rate: #ocorre mutacao
						if randrange(0,2)==1:
							element.x[j]=round(element.x[j]+mutation_intensity*element.x[j], DECIMAL_APPROX)
						else:
							element.x[j]=round(element.x[j]-mutation_intensity*element.x[j], DECIMAL_APPROX)


def main():
	test = Population(POPULATION_SIZE, DIMENSIONS)

	for i in range(1000):
		test.evolve(ackley, 0.2)

	





if __name__ == '__main__': main()