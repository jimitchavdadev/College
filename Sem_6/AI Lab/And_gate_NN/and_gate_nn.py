import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        self.weights = np.zeros(input_size + 1)  # Including bias
        self.learning_rate = learning_rate
        self.epochs = epochs
    
    def activation_function(self, x):
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        x_with_bias = np.insert(x, 0, 1)  # Adding bias term
        weighted_sum = np.dot(self.weights, x_with_bias)
        return self.activation_function(weighted_sum)
    
    def train(self, X, y):
        for _ in range(self.epochs):
            for i in range(len(X)):
                x_with_bias = np.insert(X[i], 0, 1)  # Adding bias term
                prediction = self.predict(X[i])
                error = y[i] - prediction
                self.weights += self.learning_rate * error * x_with_bias  # Weight update rule

# Training data for AND gate
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

# Create perceptron and train it
perceptron = Perceptron(input_size=2)
perceptron.train(X, y)

# Testing
for inputs in X:
    print(f"Input: {inputs}, Output: {perceptron.predict(inputs)}")