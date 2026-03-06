# Consider below task
    # Train linear regression model
    # Predict salary for 6 years of experience
    # Plot regression line using matplotlib

# Dataset
# Experience = [1, 2, 3, 4, 5]
# Salary     = [20000, 25000, 30000, 35000, 40000]

# Expected output
    # Predicted Salary for 6 years experiences : 45000

# Graph should display:
    # Data points
    # Regression line

import numpy as np
import matplotlib.pylab as plt

def Calculate_Mean(data):
    total = 0
    
    for num in data:
        total = total + num
    
    mean = total / len(data)
    
    return mean

def Calculate_Y_Predicted(X, m, C):
    Y_Pred = []

    for i in range(len(X)):
        res = m * X[i] + C
        Y_Pred.append(res)

    return Y_Pred

def Calculate_MSE(Y, Y_pred):
    numerator = 0
    denominator = len(Y)

    for i in range(len(Y)):
        numerator = numerator + ((Y[i] - Y_pred[i])  ** 2)

    MSE = numerator/denominator

    return MSE

def Calculate_RSquare(Y_pred, Y_mean, Y):
    numerator = 0
    denominator = 0

    for i in range(len(Y)):
        numerator = numerator + ((Y_pred[i] - Y_mean)  ** 2)
        denominator = denominator + ((Y[i] - Y_mean)  ** 2)

    R_square = numerator/denominator

    return R_square

def MarvellousPredictor():
    # Load the data
    X = [1, 2, 3, 4, 5]
    Y = [20000, 25000, 30000, 35000, 40000]

    print("Values of Independent variables : X -", X)
    print("Values of Dependent variables : Y -", Y)

    mean_x = Calculate_Mean(X)
    mean_y = Calculate_Mean(Y)

    print("X_MEAN is :", mean_x)        # 3.0
    print("Y_MEAN is :", mean_y)        # 30000.0

    n = len(X)      # 5

    # Y = mX + C

    # m = (summ(X - X_bar) * (Y - Y_bar)) / (Summ (X - X_bar) ** 2)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x)  ** 2)

    # slope (m)
    m = numerator / denominator

    print("Slope of line i.e m :", m)       # 5000.0

    C = mean_y - (m * mean_x)           # Y = mX + C
    print("Y intercept of line i.e C :", C)     # 15000.0 

    Y_predicted = Calculate_Y_Predicted(X, m, C)
    print("Predicted values using regression equation : Yp", Y_predicted)       # [20000.0, 25000.0, 30000.0, 35000.0, 40000.0]

    MeanSquareError = Calculate_MSE(Y, Y_predicted)
    print("Mean Square Error value is :", MeanSquareError)  # 0.0

    R_square = Calculate_RSquare(Y_predicted, mean_y, Y)
    print("R square score is :", R_square)                  # 1.0

    x = np.linspace(1, 6, n)  # 1 pasun 6 prynt print kr tyala n number de
    y = C + m * x

    plt.plot(x, y, color='g', label='Regression Line')
    plt.scatter(X, Y, color='r', label='Scatter Plot')

    plt.xlabel("X : Independent variables")
    plt.ylabel("Y : Dependent variables")

    plt.legend()
    plt.show()

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()