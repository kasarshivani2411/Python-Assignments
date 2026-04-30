# Write a Python program to calculate the Loss manually
# Tasks:
# 1. Implement Mean Squared Error
# 2. Implement Binary Cross Entropy
# 3. Take Actual and Predicted values
# 4. Display the calculated loss
# 5. Explain which loss function is used for regression and classification


# ---------------------------------------------------------
# Program : calculate the Loss manually
# Author  : Shivani Rajendra Kasar
# ---------------------------------------------------------

import math

# ---------------------------------------------------------
# Mean Squared Error (MSE)
# ---------------------------------------------------------
def mean_squared_error(y_actual, y_predicted):
    n = len(y_actual)
    total_error = 0

    for i in range(n):
        error = y_actual[i] - y_predicted[i]
        total_error += error ** 2   # Squared error

    mse = total_error / n
    return mse

# ---------------------------------------------------------
# Binary Cross Entropy (BCE)
# ---------------------------------------------------------
def binary_cross_entropy(y_actual, y_predicted):
    total_loss = 0
    n = len(y_actual)

    for i in range(n):
        y = y_actual[i]
        p = y_predicted[i]

        # Avoid log(0)
        p = max(min(p, 0.999), 0.001)

        loss = -(y * math.log(p) + (1 - y) * math.log(1 - p))
        total_loss += loss

    return total_loss / n

# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------
def main():

    print("\n-------- Loss Function Calculation --------\n")

    # Taking input
    y_actual = [1, 0, 1]
    y_predicted = [0.9, 0.2, 0.8]

    # y_actual = list(map(float, input("Enter y_actual values (space separated): ").split()))
    # y_predicted = list(map(float, input("Enter y_predicted values (space separated): ").split()))

    if len(y_actual) != len(y_predicted):
        print("Error: Length mismatch!")
        return

    # Calculate losses
    mse = mean_squared_error(y_actual, y_predicted)
    bce = binary_cross_entropy(y_actual, y_predicted)

    # Display results
    print("\n--------- Results ---------")
    print("Mean Squared Error (MSE):", mse)
    print("Binary Cross Entropy (BCE):", bce)

if __name__ == "__main__":
    main()


# MSE loss function used for Regression problems
# BCE loss function used for Binary Classification