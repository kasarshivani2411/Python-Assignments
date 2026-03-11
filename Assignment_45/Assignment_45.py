import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    border = "-"*40

    #-------------------------------------------------------
    # Step 1 : Get Data
    #-------------------------------------------------------

    print(border)
    print("Step 1 : Load the dataset")
    print(border)

    df = pd.read_csv(DataPath)
    print(border)
    print("Few entries fromm the dataset")
    print(df.head())
    print(border)

    #-------------------------------------------------------
    # Step 2 : Clean, Prepare and Manipulate the dataset
    #-------------------------------------------------------

    print(border)
    print("Step 2 : Clean, Prepare and Manipulate the dataset")
    print(border)

    df.dropna(inplace=True)                   
    print("Total records :", df.shape[0])
    print("Total columns :", df.shape[1])
    print(border)

    #-------------------------------------------------------
    # Separate independent and dependent variables
    #-------------------------------------------------------

    print(border)
    print("Separate independent and dependent variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(border)
    print("Input columns :", X.columns.to_list())
    print("Output columns : Class")

    #-------------------------------------------------------
    # Split the dataset for training and testing
    #-------------------------------------------------------

    print(border)
    print("Split the dataset for training and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)     

    print(border)
    print("Information of training and testing data")
    print("X_train shape", X_train.shape)
    print("X_test shape", X_test.shape)
    print("Y_train shape", Y_train.shape)
    print("Y_test shape", Y_test.shape)
    print(border)

    #-------------------------------------------------------
    # Feature Scaling
    #-------------------------------------------------------

    print(border)
    print("Feature Scaling")
    print(border)

    scalar = StandardScaler()
    # Independent variable scaling
    X_train_Scaled = scalar.fit_transform(X_train)
    X_test_Scaled = scalar.fit_transform(X_test)\
    
    print("Feature scaling is done")

    #-------------------------------------------------------
    # Explore multiple values of K
    #-------------------------------------------------------

    # Hyperparameter tuning (K)
    print(border)
    print("Explore multiple values of K")
    print(border)

    accuracy_scores = []
    K_values = range(1, 21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_Scaled, Y_train)
        Y_pred = model.predict(X_test_Scaled)
        accuracy = accuracy_score(Y_test, Y_pred)
        accuracy_scores.append(accuracy)

    print(border)
    print("Accuracy report of all K values from 1 to 20")
    for value in accuracy_scores:
        print(value)
        
    print(border)

    #-------------------------------------------------------
    # Plot graph of K vs Accuracy
    #-------------------------------------------------------

    print(border)
    print("Plot graph of K vs Accuracy")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values, accuracy_scores, marker = 'o')
    plt.title("K values vs Accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()

    #-------------------------------------------------------
    # Finding best value of K
    #-------------------------------------------------------

    print(border)
    print("Finding best value of K")
    print(border)

    best_K = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of K is :", best_K)

    #-------------------------------------------------------
    # Build final model using best value of K
    #-------------------------------------------------------

    print(border)
    print("Build final model using best value of K")
    print(border)

    final_model = KNeighborsClassifier(n_neighbors=best_K)

    #-------------------------------------------------------
    # Step 3 : Train the data
    #-------------------------------------------------------

    final_model.fit(X_train_Scaled, Y_train)

    #-------------------------------------------------------
    # Step 4 : Test the data
    #-------------------------------------------------------

    Y_pred = final_model.predict(X_test_Scaled)

    #-------------------------------------------------------
    # Step 5 : Calculate the Accuracy
    #-------------------------------------------------------

    print(border)
    print("Step 5 : Calculate the accuracy")
    print(border)

    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of model is :", accuracy*100)

    #-------------------------------------------------------
    # Display confusion matrix
    #-------------------------------------------------------

    print(border)
    print("Display confusion matrix")
    print(border)

    cm = confusion_matrix(Y_test, Y_pred)
    print(cm)

    #-------------------------------------------------------
    # Display classification report
    #-------------------------------------------------------

    print(border)
    print("Display classification report")
    print(border)

    print(classification_report(Y_test, Y_pred))

def main():
    border = "-"*40

    print(border)
    print("Wine Classifier using KNN")
    print(border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()