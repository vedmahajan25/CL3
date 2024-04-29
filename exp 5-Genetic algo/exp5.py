
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from geneticalgorithm import geneticalgorithm as ga

# Generate synthetic dataset for spray drying of coconut milk
num_samples = 1000
X = np.random.rand(num_samples, 5)  # Features
y = np.random.rand(num_samples)      # Target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network model
def create_model(layers, activation):
    activation_functions = ['identity', 'logistic', 'tanh', 'relu']
    chosen_activation = activation_functions[int(round(activation * (len(activation_functions) - 1)))]
    layers = [int(round(layer)) for layer in layers]  # Ensure layers are integers
    model = MLPRegressor(hidden_layer_sizes=tuple(layers), activation=chosen_activation, random_state=42)
    return model

# Define the objective function to be minimized
def objective_function(params):
    layers = params[0:3]  # Number of neurons in each hidden layer
    activation = params[3]  # Activation function

    model = create_model(layers, activation)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    return mse

# Define the bounds and constraints for the genetic algorithm parameters
varbound = np.array([[10, 100], [10, 100], [10, 100], [0, 1]])  # Bounds for neurons in each layer and activation function
vartype = np.array([['int'], ['int'], ['int'], ['real']])  # Variable type: integer for neurons, real for activation function

# Initialize and run the genetic algorithm with modified settings for a quick test
algorithm_param = {
    'max_num_iteration': 20,      # Only one iteration for testing
    'population_size': 10,       # Smaller population size for testing
    'max_iteration_without_improv': 10,
    'crossover_type': 'uniform',
    'elit_ratio': 0.02,
    'crossover_probability': 0.9,
    'mutation_probability': 0.1,
    'parents_portion': 0.5
}

model = ga(function=objective_function, dimension=4, variable_type_mixed=vartype, variable_boundaries=varbound, algorithm_parameters=algorithm_param)
model.run()

# Get the best parameters and minimum MSE
best_params = model.output_dict['variable']
best_mse = model.output_dict['function']

print("Best parameters found:", best_params)
print("Minimum MSE:", best_mse)
