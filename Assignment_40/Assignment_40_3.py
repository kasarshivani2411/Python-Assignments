# 1. After training the decision tree Model, use:
# model.feature_importances_
#     1) Display importance score of each feature.
#     2) Which feature contributes the most in predicting FinalResult?
#     3) Which feature contributes the least?

# 2. Remove the column SleepHours from the dataset.
#     1) Train the model again.
#     2) Compare new accuracy with previous accuracy.
#     3) Does removing this feature affect performance?

# 3. Train the model using only:
#     1) StudyHours
#     2) Attendance

# Compare the accuracy with the full-feature model.
# Is the model still performing well?

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
# Step 1 : Dataset Loading
###########################################################################################

print(Border)
print("Step 1 : Dataset Loading")
print(Border)

DatasetPath = "student_performance_ml.csv"
df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully...")

###########################################################################################
# Step 2 : Data Analysis
###########################################################################################

print(Border)
print("Step 2 : Data Analysis")
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
# Define Independent and Dependent Variable
###########################################################################################

print(Border)
print("Define Independent and Dependent Variable")
print(Border)

# X : Independent Variables / Features
# Y : Dependent Variables / Labels

feature_cols = ["StudyHours", "Attendance", "PreviousScore", "SleepHours", "AssignmentsCompleted"]

X = df[feature_cols]
Y = df["FinalResult"]

print("X shape :", X.shape)
print("Y shape :", Y.shape)

###########################################################################################
# Step 3 : Data Visualization
###########################################################################################

print(Border)
print("Step 3 : Data Visualization")
print(Border)

plt.figure(figsize=(8,6))

# Separate data based on FinalResult
for result in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == result]
    
    if result == 0:
        label_name = "Fail (0)"
        color = "red"
    else:
        label_name = "Pass (1)"
        color = "green"
    
    plt.scatter(
        temp["StudyHours"],
        temp["PreviousScore"],
        label=label_name,
        color=color,
        s=60
    )

plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.legend()
plt.grid(True)
plt.show()

###########################################################################################
# Step 4 : Split the dataset for training and testing
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
# Build the model
###########################################################################################

print(Border)
print("Build the model")
print(Border)

print("We are going to use DecisionTreeClassifier")

model = DecisionTreeClassifier(
    criterion= "gini",
    # max_depth= 1,
    # max_depth= 3,
    max_depth= None,
    random_state= 42
)

print("Model successfully created :", model)

# Model gives the same accuracy for all max_depth values

###########################################################################################
# Step 5 : Model Training
###########################################################################################

print(Border)
print("Step 5 : Model Training")
print(Border)

model.fit(X_train, Y_train)

print("Model training completed")

###########################################################################################
# Step 6 : Prediction
###########################################################################################

print(Border)
print("Step 6 : Prediction")
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
# Step 7: Accuracy calculation
###########################################################################################

print(Border)
print("Step 7: Accuracy calculation")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy of model :", accuracy*100)

cm = confusion_matrix(Y_test, Y_pred)

print("Confusion matrix : ")
print(cm)

print("Classification Report : ")
print(classification_report(Y_test, Y_pred))

###########################################################################################
# Step 8 : Confusion matrix generation
###########################################################################################

print(Border)
print("Step 8 : Confusion matrix generation")
print(Border)

data = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
data.plot()
plt.title("Confusion Matrix of Student performance dataset")
plt.show()

###########################################################################################
# Step 9 : Final Conclusion
###########################################################################################

print(Border)
print("Training vs Testing Accuracy")
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

###########################################################################################
# Train Model Using Only StudyHours and Attendance
###########################################################################################

print(Border)
print("Train Model Using Only StudyHours and Attendance")
print(Border)

feature_cols_two = ["StudyHours", "Attendance"]

X_two = df[feature_cols_two]
Y_two = df["FinalResult"]

# Split dataset
X_train_two, X_test_two, Y_train_two, Y_test_two = train_test_split(
    X_two,
    Y_two,
    test_size=0.2,
    random_state=42
)

# Create new model
model_two = DecisionTreeClassifier(
    criterion="gini",
    max_depth=None,
    random_state=42
)

# Train the model
model_two.fit(X_train_two, Y_train_two)

# Test the model
Y_pred_two = model_two.predict(X_test_two)

# Accuracy calculation
accuracy_two = accuracy_score(Y_test_two, Y_pred_two)

print(f"Previous Testing Accuracy (All Features) : {test_accuracy*100:.2f}%")
print(f"Testing Accuracy (Only 2 Features)       : {accuracy_two*100:.2f}%")

# Compare performance
print("\nPerformance Comparison:")
if accuracy_two < test_accuracy:
    print("Accuracy decreased when using only StudyHours and Attendance.")
elif accuracy_two > test_accuracy:
    print("Accuracy improved when using only StudyHours and Attendance.")
else:
    print("Accuracy remains the same with only two features.")

# Is the model still performing well?
# Yes