# Write a Python program to simulate a single artificial neuron
# Input : x1 = 2, x2 = 3, w1 = 0.4, w2 = 0.6, bias = 0.5

# Tasks :
# 1. Calculate the weighted sum
# 2. Apply sigmoid activation function
# 3. Display final output
# 4. Explain whether output is close to 0 or 1

# ---------------------------------------------------------
# Program : Single Artificial Neuron with Sigmoid Activation
# Author  : Shivani Rajendra Kasar
# ---------------------------------------------------------

import math
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# Sigmoid Activation Function
# ---------------------------------------------------------
# Sigmoid converts input into range (0, 1)
# Used for probability-based outputs

def sigmoid(z):
    # Sigmoid Function
    # Formula: 1 / (1 + e^(-z))

    return 1 / (1 + math.exp(-z))

# ---------------------------------------------------------
# Neuron Forward Pass
# ---------------------------------------------------------
# Marvellous_neuron_forward_propogation() function Performs:
# 1. Weighted sum
# 2. Add bias
# 3. Apply sigmoid activation

def Marvellous_neuron_forward_propogation(inputs, weights, bias):

    print("\n----- Neuron Calculation Started -----\n")

    # Display inputs
    print("Inputs (x)   :", inputs)
    print("Weights (w)  :", weights)
    print("Bias (b)     :", bias)

    # -----------------------------------------------------
    # Weighted Sum Calculation
    # z = w·x + b
    # -----------------------------------------------------

    z = sum(w * x for w, x in zip(weights, inputs)) + bias

    print("\nStep 1: Weighted Sum")
    print("z =", z)

    # -----------------------------------------------------
    # Apply Sigmoid Activation
    # -----------------------------------------------------

    y_hat = sigmoid(z)

    print("\nStep 2: Activation Function")
    print("Activation Function used : Sigmoid")
    print("Output (ŷ) =", y_hat)

    print("\n----- Neuron Calculation Ended -----\n")

    return z, y_hat


# ---------------------------------------------------------
# Plot Sigmoid Function
# ---------------------------------------------------------

def plot_sigmoid():

    # Generate input range
    z_values = np.linspace(-10, 10, 200)

    # Apply sigmoid on range
    sigmoid_values = 1 / (1 + np.exp(-z_values))

    # Plot graph
    plt.figure(figsize=(8, 5))
    plt.plot(z_values, sigmoid_values, label="Sigmoid Function", linewidth=2, color="blue")

    # Reference lines
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axhline(y=1, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")

    # Labels and title
    plt.title("Sigmoid Activation Function", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output (Probability)", fontsize=14)

    # Grid and legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    plt.show()

# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    print("\n----------- Sigmoid Neuron -----------\n")

    # Inputs
    inputs = [2, 3]

    # Weights
    weights = [0.4, 0.6]

    # Bias
    bias = 0.5

    # Forward pass
    z, y_hat = Marvellous_neuron_forward_propogation(inputs, weights, bias)

    print("Final z     :", z)
    print("Final y_hat :", y_hat)

    # Plot graph
    plot_sigmoid()

if __name__ == "__main__":
    main()

# ---------------------------------------------------------
# Explain whether output is close to 0 or 1
# ---------------------------------------------------------
# Final y_hat = 0.9568927450589139, so output value is near to 1