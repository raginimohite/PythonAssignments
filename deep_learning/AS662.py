# Program to demonstrate different activation functions

import numpy as np
import matplotlib.pyplot as plt

# Input values from -10 to 10
x = np.linspace(-10, 10, 100)

# 1. Sigmoid Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 2. ReLU Function
def relu(x):
    return np.maximum(0, x)

# 3. Tanh Function
def tanh(x):
    return np.tanh(x)

# Calculate activation values
y_sigmoid = sigmoid(x)
y_relu = relu(x)
y_tanh = tanh(x)

# Plot Sigmoid
plt.figure(figsize=(6, 4))
plt.plot(x, y_sigmoid)
plt.title("Sigmoid Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()

# Plot ReLU
plt.figure(figsize=(6, 4))
plt.plot(x, y_relu)
plt.title("ReLU Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()

# Plot Tanh
plt.figure(figsize=(6, 4))
plt.plot(x, y_tanh)
plt.title("Tanh Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid()
plt.show()