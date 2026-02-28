# 1. Import DecisionTreeClassifier from sklearn.
# Create a model object and train it using fit().

# 2. Use the trained model to predict results for X_test.
# Display predicted values along with actual values.

# 3. Calculate model accuracy using accuracy_score.
# Display the result in percentage format.

# 4. Generate confusion matrix using sklearn.
# Display it using confusionMatrixDisplay.
# Explain clearly:
#     a. True Positive
#     b. True Negative
#     c. False Positive
#     d. False Negative

# 5. Calculate:
#     a. Training accuracy
#     b. Testing accuracy
# Compare both and comment whether the model is overfitting or underfitting.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, 
    confusion_matrix, 
    classification_report,
    ConfusionMatrixDisplay
)
import matplotlib.pyplot as plt

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

###########################################################################################
# Step 8 : Test / Evaluate the model
###########################################################################################

print(Border)
print("Step 8 : Test / Evaluate the model")
print(Border)

Y_pred = model.predict(X_test)

print("Model evaluation (testing) completed")
print(Y_pred.shape)

print("Expected Answers : ")
print(Y_test)
# print(list(Y_test))

print("Predicted Answers : ")
print(Y_pred)

results_df = pd.DataFrame({
    "Actual": Y_test.values,
    "Predicted": Y_pred
})

print("\nPredicted vs Actual Results:")
print(results_df)

###########################################################################################
# Step 9 : Evaluate the model performance
###########################################################################################

print(Border)
print("Step 9 : Evaluate the model performance")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy of model :", accuracy*100)

cm = confusion_matrix(Y_test, Y_pred)

print("Confusion matrix : ")
print(cm)

print("Classification Report : ")
print(classification_report(Y_test, Y_pred))

###########################################################################################
# Step 10 : Plot confusion matrix
###########################################################################################

print(Border)
print("Step 10 : Plot confusion matrix")
print(Border)

data = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
data.plot()
plt.title("Confusion Matrix of Student performance dataset")
plt.show()

###########################################################################################
# Step 11 : Calculate Training and Testing Accuracy & Check Overfitting/Underfitting
###########################################################################################

print(Border)
print("Step 11 : Training vs Testing Accuracy")
print(Border)

# a. Training Accuracy
train_pred = model.predict(X_train)
train_accuracy = accuracy_score(Y_train, train_pred)
print(f"Training Accuracy : {train_accuracy*100:.2f}%")

# b. Testing Accuracy
test_accuracy = accuracy_score(Y_test, Y_pred)
print(f"Testing Accuracy  : {test_accuracy*100:.2f}%")

# Compare and comment
print("\nAnalysis:")
if train_accuracy > test_accuracy + 0.05:  # more than 5% gap
    print("The model shows signs of overfitting: performs much better on training data than testing data.")
elif test_accuracy > train_accuracy + 0.05:
    print("The model shows signs of underfitting: performs better on unseen data, may indicate training issues.")
else:
    print("The model has balanced performance: no significant overfitting or underfitting detected.")