import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousAdvertise(DataPath):
    Border = "-"*40
    #-----------------------------------------------------------------
    # Step 1 : Get Data
    #-----------------------------------------------------------------

    print(Border)
    print("Step 1 : Load the Data")
    print(Border)

    df = pd.read_csv(DataPath)

    print("Some records from the dataset : ")
    print(df.head())

    #-----------------------------------------------------------------
    # Step 2 : Clean, Prepare and Manipulate data
    #-----------------------------------------------------------------

    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate data")
    print(Border)

    print("Shape of dataset before removal : ", df.shape)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    print("Shape of dataset after removal : ", df.shape)

    print(Border)
    print("Clean dataset is : ")
    print(Border)

    print(df.head())

    print(Border)
    print("Check missing values")
    print(Border)

    print("Missing values count :\n", df.isnull().sum())

    print(Border)
    print("Statistical Summary")
    print(Border)

    print(df.describe())

    print(Border)
    print("Correlation between columns")
    print(Border)

    print("Correlation Matrix")
    print(df.corr())

    print(Border)
    print("Split dataset into independent and dependent variables")
    print(Border)

    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    print("Shape of independent variables : ", X.shape)
    print("Shape of dependent variables : ", Y.shape)

    print(Border)
    print("Split dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    print("X_train Shape : ", X_train.shape)
    print("X_test Shape : ", X_test.shape)
    print("Y_train Shape : ", Y_train.shape)
    print("Y_test Shape : ", Y_test.shape)

    #-----------------------------------------------------------------
    # Step 3 : Train the Model
    #-----------------------------------------------------------------

    print(Border)
    print("Step 3 : Train the Model/Data")
    print(Border)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    #-----------------------------------------------------------------
    # Step 4 : Test the Model
    #-----------------------------------------------------------------

    print(Border)
    print("Step 4 : Test the Model/Data")
    print(Border)

    Y_pred = model.predict(X_test)

    print(Border)
    print("Evaluate the Model")
    print(Border)

    MSE = mean_squared_error(Y_test, Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test, Y_pred)

    print("Mean squared error :", MSE)
    print("Root Mean squared error :", RMSE)
    print("R square value :", R2)

    print(Border)
    print("Calculate Model Coefficient")
    print(Border)

    for column, value in zip(X.columns, model.coef_):
        print(f"{column} : {value}")

    print("Intercept :", model.intercept_)

    #-----------------------------------------------------------------
    # Step 5 : Compare and Display the actual and predicted values
    #-----------------------------------------------------------------

    print(Border)
    print("Step 5 : Compare and Display the actual and predicted values")
    print(Border)

    Result = pd.DataFrame({
        'Actual sale' : Y_test.values,
        'Predicted sale' : Y_pred
        })
    
    print(Result.head())

    print(Border)
    print("Plot actual vs predicted")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.scatter(Y_test, Y_pred)
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")
    plt.title("Actual sales vs Predicted sales")
    plt.grid(True)
    plt.show()

def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()