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

# 4. Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their results.
# Displat predictions clearly.

# 5. Without using accuracy_score, manually calculate accuracy:
# Verify whether it matches sklearn accuracy.

# 6. Identify students where:
# Y_test != Y_pred
#     1) Display those rows.
#     2) How many students were misclassified?
#     3) What common pattern do you observe?

# 7. Train model using:
#     1) random_state = 0
#     2) random_state = 10
#     3) random_state = 42

# Compare testing accuracy.
# Does the result change?

# 8. Decision Tree Visualization
# Use:
# from sklearn.tree import plot_tree
# Visualize the trained decision tree.
#     1) Which feature appears at the root node?
#     2) Why do you think that feature was selected first?

# 9. Create a new column:
# PerformanceIndex = (StudyHours * 2) + Attendance

# Train the model including this new feature.
# Does accuracy improve?

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
    # random_state = 0
    # random_state = 10
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
    # random_state = 0
    # random_state = 10
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
# Manual Accuracy Calculation
###########################################################################################

print(Border)
print("Manual Accuracy Calculation")
print(Border)

# Count correct predictions
correct_predictions = (Y_test.values == Y_pred).sum()

# Total predictions
total_predictions = len(Y_test)

# Manual accuracy formula
manual_accuracy = correct_predictions / total_predictions

print(f"Correct Predictions : {correct_predictions}")
print(f"Total Predictions   : {total_predictions}")
print(f"Manual Accuracy     : {manual_accuracy*100:.2f}%")

# Compare with sklearn accuracy
print(f"Sklearn Accuracy    : {accuracy*100:.2f}%")

# Verification
if abs(manual_accuracy - accuracy) < 1e-6:
    print("Manual accuracy matches sklearn accuracy.")
else:
    print("Manual accuracy does NOT match sklearn accuracy.")

# Manual accuracy matches sklearn accuracy.

###########################################################################################
# Identify Misclassified Students
###########################################################################################

print(Border)
print("Identify Misclassified Students")
print(Border)

# Create comparison DataFrame
comparison_df = pd.DataFrame({
    "StudyHours": X_test["StudyHours"].values,
    "Attendance": X_test["Attendance"].values,
    "PreviousScore": X_test["PreviousScore"].values,
    "SleepHours": X_test["SleepHours"].values,
    "AssignmentsCompleted": X_test["AssignmentsCompleted"].values,
    "Actual": Y_test.values,
    "Predicted": Y_pred
})

# Filter misclassified rows
misclassified = comparison_df[comparison_df["Actual"] != comparison_df["Predicted"]]

print("Misclassified Students:")
print(misclassified)

# Count misclassified students
num_misclassified = len(misclassified)
print(f"\nNumber of Misclassified Students: {num_misclassified}")

# Percentage of misclassification
misclassification_rate = (num_misclassified / len(Y_test)) * 100
print(f"Misclassification Rate: {misclassification_rate:.2f}%")

# Yes. The testing accuracy changes depending on random_state

###########################################################################################
# Decision Tree Visualization
###########################################################################################

print(Border)
print("Decision Tree Visualization")
print(Border)

from sklearn.tree import plot_tree

plt.figure(figsize=(18,10))

plot_tree(
    model,
    feature_names=feature_cols,
    class_names=["Fail (0)", "Pass (1)"],
    filled=True,
    rounded=True,
    fontsize=10
)

plt.title("Decision Tree Visualization")
plt.show()

# 1) Which feature appears at the root node?
# Attendance is the root node feature.

# 2) Why do you think that feature was selected first?
# Because splitting on Attendance at 75.5 produces the highest reduction in impurity (Gini impurity). 
# It best separates the students into Fail and Pass classes with very pure leaf nodes (Gini = 0.0 in children), 
# making it the most informative first split for this dataset.

# 9

###########################################################################################
# New feature PerformanceIndex
###########################################################################################

print(Border)
print("Adding new feature PerformanceIndex")
print(Border)

# Create PerformanceIndex = (StudyHours * 2) + Attendance
df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

# Define new feature columns including PerformanceIndex
new_feature_cols = feature_cols + ["PerformanceIndex"]

# Prepare new X and Y
X_new = df[new_feature_cols]
Y_new = df["FinalResult"]

print("New feature columns:", new_feature_cols)

###########################################################################################
# Split data with new feature and retrain model
###########################################################################################

print(Border)
print("Split data and train model with new feature")
print(Border)

X_train_new, X_test_new, Y_train_new, Y_test_new = train_test_split(
    X_new,
    Y_new,
    test_size=0.2,
    random_state=42
)

model_new = DecisionTreeClassifier(
    criterion="gini",
    max_depth=None,
    random_state=42
)

model_new.fit(X_train_new, Y_train_new)

print("Model retrained with new feature PerformanceIndex")

###########################################################################################
# Prediction and Accuracy Calculation with new feature
###########################################################################################

print(Border)
print("Prediction and accuracy with new feature")
print(Border)

Y_pred_new = model_new.predict(X_test_new)

accuracy_new = accuracy_score(Y_test_new, Y_pred_new)
print(f"Accuracy with new feature PerformanceIndex: {accuracy_new*100:.2f}%")

###########################################################################################
# Compare old and new accuracy
###########################################################################################

print(Border)
print("Compare Accuracy")
print(Border)

print(f"Old accuracy: {accuracy*100:.2f}%")
print(f"New accuracy: {accuracy_new*100:.2f}%")

if accuracy_new > accuracy:
    print("Accuracy improved after adding PerformanceIndex.")
elif accuracy_new < accuracy:
    print("Accuracy decreased after adding PerformanceIndex.")
else:
    print("Accuracy remained the same after adding PerformanceIndex.")

# Accuracy remained the same after adding PerformanceIndex.