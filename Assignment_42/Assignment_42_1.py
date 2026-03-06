# Implement Simple Linear Regression manually without using any ML library.

# Dataset
# X = [1, 2, 3, 4, 5]
# Y = [3, 4, 2, 4, 5]

# Tasks
    # Calculate
        # Mean of X (X bar)
        # Mean of Y (Y bar)
        # Slope (m)
        # Intercept (c)

# Expected Output Examples
    # Mean of X = 3
    # Mean of Y = 3.6

    # Slope (m) = 0.4
    # Intercept (c) = 2.4

    # Regression Equation : 
    # Y = 0.4X + 2.4

    # Predicted Y for X = 6 : 4.8

def CalculateMean(data):
    total = 0
    
    for num in data:
        total = total + num
    
    mean = total / len(data)
    
    return mean

def MarvellousPredictor():
    # Load the data
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    print("Values of Independent variables : X -", X)
    print("Values of Dependent variables : Y -", Y)

    mean_x = CalculateMean(X)
    mean_y = CalculateMean(Y)

    print("X_MEAN is :", mean_x)        # 3.0
    print("Y_MEAN is :", mean_y)        # 3.6

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

    print("Slope of line i.e m :", m)       # 0.4

    C = mean_y - (m * mean_x)           # Y = mX + C

    print("Y intercept of line i.e C :", C)     # 2.4 

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()