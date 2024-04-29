import numpy as np

class ClonalSelectionAlgorithm:
    def __init__(self, objective_function, num_variables, num_population=100, num_clones=10, mutation_rate=0.1, max_generations=100):
        self.objective_function = objective_function
        self.num_variables = num_variables
        self.num_population = num_population
        self.num_clones = num_clones
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations

    def initialize_population(self):
        return np.random.rand(self.num_population, self.num_variables)

    def clone(self, population, fitness):
        num_selected = int(self.num_clones / 2)
        sorted_indices = np.argsort(fitness)
        selected_population = population[sorted_indices[:num_selected]]
        return np.repeat(selected_population, self.num_clones // num_selected, axis=0)

    def mutate(self, clones):
        mutation_mask = np.random.rand(*clones.shape) < self.mutation_rate
        mutations = np.random.rand(*clones.shape) * 0.1  # Adjust mutation range based on problem domain
        clones[mutation_mask] += mutations[mutation_mask]
        return clones

    def select(self, clones, population, fitness):
        merged_population = np.vstack((population, clones))
        merged_fitness = np.concatenate((fitness, self.objective_function(clones)))
        sorted_indices = np.argsort(merged_fitness)
        selected_population = merged_population[sorted_indices[:self.num_population]]
        selected_fitness = merged_fitness[sorted_indices[:self.num_population]]
        return selected_population, selected_fitness
        
        # Ensure the size of merged_fitness is not greater than num_population
        if len(merged_fitness) > self.num_population:
            merged_fitness = merged_fitness[:self.num_population]

        return merged_population[sorted_indices[:self.num_population]], merged_fitness

    def optimize(self):
        population = self.initialize_population()
        best_solution = None
        best_fitness = np.inf

        for generation in range(self.max_generations):
            fitness = self.objective_function(population)
            if np.min(fitness) < best_fitness:
                best_solution = population[np.argmin(fitness)]
                best_fitness = np.min(fitness)

            clones = self.clone(population, fitness)
            clones = self.mutate(clones)
            population, fitness = self.select(clones, population, fitness)

        return best_solution, best_fitness

# Example usage:
def objective_function(x):
    return np.sum(x**2, axis=1)  # Minimize sum of squares

num_variables = 5
csa = ClonalSelectionAlgorithm(objective_function, num_variables)
best_solution, best_fitness = csa.optimize()
print("Best solution:", best_solution)
print("Best fitness:", best_fitness)
