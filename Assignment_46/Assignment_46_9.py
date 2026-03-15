# Consider the below dataset
# StudyHours = [1, 2, 3, 4, 5]
# SleepHours = [7, 6, 7, 6, 8]
# Marks = [50, 55, 60, 65, 70]

# Write a Python program to:
# Train a regression model using this dataset
# Print coefficients for both the features
# Print the intercept

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def LinearRegressionModel():
    # Load the data
    # Independent Variables 
    X = [[1, 7], [2, 6], [3, 7], [4, 6], [5, 8]]

    # Dependent variables
    Y = [50, 55, 60, 65, 70]

    print("Independent variables : X -", X)
    print("Dependent variables : Y -", Y)

    # Splitting dataset for training and testing

    X_train, X_test, Y_train, Y_test =  train_test_split(X, Y, test_size=0.2, random_state=42)

    # train the model
    model = LinearRegression()

    model.fit(X_train, Y_train)

    # Test the model
    Y_pred = model.predict(X_test)

    # Coefficient 
    print("Coefficient for StudyHours:", model.coef_[0])
    print("Coefficient for SleepHours:", model.coef_[1])

    print("Intercept :", model.intercept_)

def main():    
    LinearRegressionModel()

if __name__ == "__main__":
    main()