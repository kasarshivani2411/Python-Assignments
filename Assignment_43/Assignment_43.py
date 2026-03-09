import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def CheckAccuracy(X, Y):
    border = "-"*40

    print(border)
    print("Step 5 : Calculating Accuracy")
    print(border)

    # Split dataset into two equal parts
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    for k in range(1,6):
        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train, Y_train)

        Y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test, Y_pred)

        print("Accuracy with K =",k,"is :",accuracy*100)

def PlayPredictor(DataPath):

    border = "-"*40

    # ---------------------------------------------
    # Step 1 : Get Data
    # ---------------------------------------------

    print(border)
    print("Step 1 : Loading Data")
    print(border)

    df = pd.read_csv(DataPath)

    print("Play Predictor Dataset : ")
    print(df)

    # ---------------------------------------------
    # Step 2 : Clean, Prepare and Manipulate data
    # ---------------------------------------------

    print(border)
    print("Step 2 : Clean, Prepare and Manipulate data")
    print(border)

    print("Shape of dataset before removal : ", df.shape)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    print("Shape of dataset after removal : ", df.shape)

    print(border)
    print("Clean dataset is : ")
    print(border)

    print(df.head())

    print(border)

    # Check missing values
    print("Missing values count :\n", df.isnull().sum())

    print(border)

    # Statistical Summary
    print("Display Statistical Summary : ")
    print(border)
    print(df.describe())
    print(border)

    # Data before label encoding
    X = df[['Weather', 'Temperature']]
    Y = df['Play']

    print("Data before label encoding : ")
    print(df.head())
    print(border)
    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)
    print(border)

    labelEncoded_Weather = LabelEncoder()
    labelEncoded_Temp = LabelEncoder()
    labelEncoded_Play = LabelEncoder()

    df['Weather'] = labelEncoded_Weather.fit_transform(df['Weather'])
    df['Temperature'] = labelEncoded_Temp.fit_transform(df['Temperature'])
    df['Play'] = labelEncoded_Play.fit_transform(df['Play'])

    print("Data after label encoding : ")
    print(border)
    print(df.head())

    print(border)

    # Features and label
    X = df[['Weather','Temperature']]
    Y = df['Play']

    print("Independent variables :", X.shape)
    print("Dependent variables :", Y.shape)

    # Spliting the data for training and testing
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42, stratify=Y)

    print(border)
    print("Information of training and testing data")
    print("X_train shape", X_train.shape)
    print("X_test shape", X_test.shape)
    print("Y_train shape", Y_train.shape)
    print("Y_test shape", Y_test.shape)
    print(border)

    # ---------------------------------------------
    # Step 3 : Train Data
    # ---------------------------------------------

    print(border)
    print("Step 3 : Training the model/data")
    print(border)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X, Y)

    print("Model trained successfully")

    # ---------------------------------------------
    # Step 4 : Test Data
    # ---------------------------------------------

    print(border)
    print("Step 4 : Testing the model")
    print(border)

    test_weather = labelEncoded_Weather.transform(['Sunny'])
    test_temp = labelEncoded_Temp.transform(['Mild'])

    test_data = pd.DataFrame(
        [[test_weather[0], test_temp[0]]],
        columns=['Weather','Temperature']
    )

    Y_pred = model.predict(test_data)

    prediction = labelEncoded_Play.inverse_transform(Y_pred)

    print("Prediction for Sunny & Mild :", prediction[0])

    # ---------------------------------------------
    # Step 5 : Accuracy
    # ---------------------------------------------

    CheckAccuracy(X, Y)


def main():

    border = "-"*40

    print(border)
    print("Marvellous Infosystems Play Predictor using KNN")
    print(border)

    PlayPredictor("PlayPredictor.csv")


if __name__ == "__main__":
    main()