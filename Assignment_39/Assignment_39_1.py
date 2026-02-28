# 1. Import DecisionTreeClassifier from sklearn.
# Create a model object and train it using fit().

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

Border = "-"*40

###########################################################################################
# Step 1 : Load the dataset
###########################################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully...")

###########################################################################################
# Step 2 : Data Analysis (EDA)
###########################################################################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of dataset :", df.shape)
print("Column names :", list(df.columns))

print("Missing values (Per column)")
print(df.isnull().sum())

print("Class Distribution (FinalResult count)")
print(df["FinalResult"].value_counts())

print("Statistical Report of dataset")
print(df.describe())

###########################################################################################
# Step 3 : Define Independent and Dependent Variable
###########################################################################################

print(Border)
print("Step 3 : Define Independent and Dependent Variable")
print(Border)

# X : Independent Variables / Features
# Y : Dependent Variables / Labels

feature_cols = ["StudyHours", "Attendance", "PreviousScore", "SleepHours", "AssignmentsCompleted"]

X = df[feature_cols]
Y = df["FinalResult"]

print("X shape :", X.shape)
print("Y shape :", Y.shape)

# Step 4 : Data Visualization

###########################################################################################
# Step 5 : Split the dataset for training and testing
###########################################################################################

print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size= 0.2,
    random_state= 42
)

print("Data splitting activity done : ")

print("X - Independent :", X.shape)     
print("Y - Dependent :", Y.shape)      

print("X_train :", X_train.shape)       
print("X_test :", X_test.shape)         
print("Y_train :", Y_train.shape)      
print("Y_test :", Y_test.shape)        

###########################################################################################
# Step 6 : Build the model
###########################################################################################

print(Border)
print("Step 6 : Build the model")
print(Border)

print("We are going to use DecisionTreeClassifier")

model = DecisionTreeClassifier(
    criterion= "gini",
    max_depth= 4,
    random_state= 42
)

print("Model successfully created :", model)

###########################################################################################
# Step 7 : Train the model
###########################################################################################

print(Border)
print("Step 7 : Train the model")
print(Border)

model.fit(X_train, Y_train)

print("Model training completed")