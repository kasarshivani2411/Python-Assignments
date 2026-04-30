# Write a Python program to demonstrate different activation functions.

# Functions to implement :
# 1. Sigmoid
# 2. ReLU
# 3. Tanh

# Tasks : 
# 1. Accept input values from -10 to 10
# 2. Plot all activation functions using Matplotlib
# 3. Explain the use of each activation function

# ----------------------------------------------------------------
# Program : Neuron Calculation Using Sigmoid, ReLU, Tanh functions
# Author  : Shivani Rajendra Kasar
# ----------------------------------------------------------------

import math
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# Activation Functions
# ---------------------------------------------------------

def sigmoid(z):
    """
    Sigmoid Activation Function
    Output range : (0, 1)
    Used for probability-based outputs
    """
    return 1 / (1 + math.exp(-z))

def relu(z):
    """
    ReLU Activation Function
    Output : max(0, z)
    Used in hidden layers of deep networks
    """
    return max(0, z)

def tanh(z):
    """
    Tanh Activation Function
    Output range : (-1, 1)
    Used in hidden layers of deep networks
    """
    return math.tanh(z)

# ---------------------------------------------------------
# Neuron Forward Pass
# ---------------------------------------------------------
# Generic neuron → works with any activation function

def Marvellous_neuron_forward(inputs, weights, bias, activation_func):

    print("\n-----Neuron Calculation Started -----\n")

    # Display input details
    print("Inputs (x)   :", inputs)
    print("Weights (w)  :", weights)
    print("Bias (b)     :", bias)

    # -----------------------------------------------------
    # Weighted Sum Calculation
    # z = w·x + b
    # -----------------------------------------------------
    z = sum(w * x for w, x in zip(weights, inputs)) + bias

    print("\nStep 1 : Weighted Sum")
    print("z =", z)

    # -----------------------------------------------------
    # Activation Function
    # -----------------------------------------------------
    y_hat = activation_func(z)

    print("\nStep 2 : Activation Function Applied")
    print("Activation Function :", activation_func.__name__)
    print("Output (ŷ) :", y_hat)

    print("\n-----Neuron Calculation Ended -----\n")

    return z, y_hat


# ---------------------------------------------------------
# Plot Activation Functions
# ---------------------------------------------------------

def plot_all_functions():

    z_values = np.linspace(-10, 10, 200)

    # Vectorized versions
    sigmoid_values = 1 / (1 + np.exp(-z_values))
    relu_values = np.maximum(0, z_values)
    tanh_values = np.tanh(z_values)

    plt.figure(figsize=(8, 5))

    # Plot all functions
    plt.plot(z_values, sigmoid_values, label="Sigmoid", linewidth=2)
    plt.plot(z_values, relu_values, label="ReLU", linewidth=2)
    plt.plot(z_values, tanh_values, label="Tanh", linewidth=2)

    # Reference lines
    plt.axhline(y=0, linewidth=0.5)
    # plt.axhline(y=1, linewidth=0.5)
    plt.axvline(x=0, linestyle="--")

    # Labels
    plt.title("Activation Function: Sigmoid, ReLU, Tanh", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output", fontsize=14)

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    plt.show()


# ---------------------------------------------------------
# Main function
# ---------------------------------------------------------

def main():

    print("\n--------- Activation Functions Implementation ---------\n")

    # Example data
    inputs = [1.0, 2.0, 3.0]
    weights = [0.6, 0.4, -0.2]
    bias = 0.5

    # Sigmoid neuron
    print("------------------ Sigmoid Neuron ------------------")
    Marvellous_neuron_forward(inputs, weights, bias, sigmoid)

    # ReLU neuron
    print("------------------ ReLU Neuron ------------------")
    Marvellous_neuron_forward(inputs, weights, bias, relu)

    # Tanh neuron
    print("------------------ Tanh Neuron ------------------")
    Marvellous_neuron_forward(inputs, weights, bias, tanh)

    # Plot comparison
    plot_all_functions()


if __name__ == "__main__":
    main()


# Sigmoid function:
# It used in Binary Classification case studies at the output layer to calculate the probability
# It ranges from 0 to 1

# ReLU function:
# It used in the hidden layers of the deep learning model (neural networks)
# It gives the output as max(0, z) --> means if any negative value comes in the output it consider it as 0 and keep value greater than 0 as it is.

# Tanh function:
# It used in the hidden layers of the deep learning model (neural networks)
# It ranges from -1 to 1