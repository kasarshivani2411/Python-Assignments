# Write a python program to show how the weights are updated in ANN.
# Tasks:
# 1. Take input, weight, bias, target output and learning rate.
# 2. Calculate Prediction.
# 3. Calculate Error.
# 4. Update weight using Gradient Descent Logic
# 5. Display old weight and Updated weight

# ---------------------------------------------------------
# Program : Weights updation in ANN
# Author  : Shivani Rajendra Kasar
# ---------------------------------------------------------

import math

# ---------------------------------------------------------
# Sigmoid Activation Function
# ---------------------------------------------------------
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Derivative of sigmoid
def sigmoid_derivative(output):
    return output * (1 - output)

# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------
def main():

    print("\n===== ANN Weight Update (Using Backpropagation) =====\n")

    # 1. Take inputs
    inputs = list(map(float, input("Enter input values: ").split()))
    weights = list(map(float, input("Enter weights: ").split()))

    bias = float(input("Enter bias: "))
    target = float(input("Enter target output: "))
    learning_rate = float(input("Enter learning rate: "))

    if len(inputs) != len(weights):
        print("Error: Inputs and weights must be same length!")
        return

    # Save old weights
    old_weights = weights.copy()
    old_bias = bias

    # -----------------------------------------------------
    # Step 2: Prediction (Forward Propagation)
    # -----------------------------------------------------
    z = sum(x * w for x, w in zip(inputs, weights)) + bias
    output = sigmoid(z)

    print("\n--- Prediction ---")
    print("Weighted Sum (z):", round(z, 4))
    print("Predicted Output:", round(output, 4))

    # -----------------------------------------------------
    # Step 3: Error
    # -----------------------------------------------------
    error = target - output
    print("\nError:", round(error, 4))

    # -----------------------------------------------------
    # Step 4: Gradient Descent (Backpropagation)
    # -----------------------------------------------------

    # dL/doutput
    dL_doutput = output - target

    # doutput/dz
    doutput_dz = sigmoid_derivative(output)

    # dL/dz
    dL_dz = dL_doutput * doutput_dz

    print("\n--- Weight Update ---")

    # Update each weight
    for i in range(len(weights)):
        gradient = dL_dz * inputs[i]
        weights[i] = weights[i] - learning_rate * gradient

        print(f"w{i+1}: {old_weights[i]} --> {round(weights[i], 6)}")

    # Update bias
    bias = bias - learning_rate * dL_dz
    print(f"b : {old_bias} --> {round(bias, 6)}")

if __name__ == "__main__":
    main()