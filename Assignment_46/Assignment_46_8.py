# Write a Python program using Linear Regression to train a regression model using below dataset
# 
# Study Hours [1, 2, 3, 4, 5]
# Marks [50, 55, 60, 65, 70] 

# Your program should :
    # Train the regression model
    # Print the coefficient
    # Print the intercept

# Y = mX + C
# Coeffiecient --> m
# Intercept --> C (slope)
# m = (summ(X - X_bar) * (Y - Y_bar)) / (Summ (X - X_bar) ** 2)

# Using the regression model created in the previous question, write a python program to predict
# marks for 6 study hours and display the predicted value

import numpy as np

def LinearRegressionModel():
    # Load the data
    # Independent Variables
    X = [1, 2, 3, 4, 5]

    # Dependent variables
    Y = [50, 55, 60, 65, 70]

    print("Independent variables : X -", X)
    print("Dependent variables : Y -", Y)

    X_mean = np.mean(X)
    Y_mean = np.mean(Y)

    print("X_MEAN is :", X_mean)       
    print("Y_MEAN is :", Y_mean)

    numberOfVar = len(X)     
    numerator = 0
    denominator = 0
    
    for i in range(numberOfVar):
        numerator = numerator + ((X[i] - X_mean) * (Y[i] - Y_mean))
        denominator = denominator + ((X[i] - X_mean)  ** 2)

    m = numerator / denominator

    print("Coefficient i.e m :", m)

    C = Y_mean - (m * X_mean)

    print("Intercept of line i.e C :", C)

    # Prediction for 6 study hours
    studyHours = 6
    predicted_marks = (m * studyHours) + C
    print("Predicted marks for 6 study hours :", predicted_marks)

def main():    
    LinearRegressionModel()

if __name__ == "__main__":
    main()