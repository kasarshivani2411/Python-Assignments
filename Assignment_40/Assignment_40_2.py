# 1. After training the decision tree Model, use:
# model.feature_importances_
#     1) Display importance score of each feature.
#     2) Which feature contributes the most in predicting FinalResult?
#     3) Which feature contributes the least?

# 2. Remove the column SleepHours from the dataset.
#     1) Train the model again.
#     2) Compare new accuracy with previous accuracy.
#     3) Does removing this feature affect performance?

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
# Step 10 : Feature Importance
###########################################################################################

print(Border)
print("Step 10 : Feature Importance")
print(Border)

# Get feature importance scores
importances = model.feature_importances_

# Create DataFrame for better visualization
feature_importance_df = pd.DataFrame({
    "Feature": feature_cols,
    "Importance Score": importances
})

# Sort values in descending order
feature_importance_df = feature_importance_df.sort_values(
    by="Importance Score",
    ascending=False
)

print("Feature Importance Scores:")
print(feature_importance_df)

# Identify most and least important features
most_important = feature_importance_df.iloc[0]
least_important = feature_importance_df.iloc[-1]

print("\nMost Important Feature:")
print(f"{most_important['Feature']} "
      f"(Score: {most_important['Importance Score']:.4f})")

print("\nLeast Important Feature:")
print(f"{least_important['Feature']} "
      f"(Score: {least_important['Importance Score']:.4f})")

# Optional: Plot Feature Importance
plt.figure(figsize=(8,5))
plt.barh(feature_importance_df["Feature"], 
         feature_importance_df["Importance Score"])
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.title("Feature Importance in Decision Tree Model")
plt.gca().invert_yaxis()
plt.grid(True)
plt.show()


# Most Important Feature:
# PreviousScore (Score: 0.41)

# Least Important Feature:
# SleepHours (Score: 0.05)


###########################################################################################
# Remove SleepHours and Retrain Model
###########################################################################################

print(Border)
print("Remove SleepHours and Retrain Model")
print(Border)

# Remove SleepHours from feature list
feature_cols_new = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted"]

X_new = df[feature_cols_new]
Y_new = df["FinalResult"]

# Split again
X_train_new, X_test_new, Y_train_new, Y_test_new = train_test_split(
    X_new,
    Y_new,
    test_size=0.2,
    random_state=42
)

# Create new model
model_new = DecisionTreeClassifier(
    criterion="gini",
    max_depth=None,
    random_state=42
)

# Train new model
model_new.fit(X_train_new, Y_train_new)

# Predict
Y_pred_new = model_new.predict(X_test_new)

# Calculate new accuracy
new_accuracy = accuracy_score(Y_test_new, Y_pred_new)

print(f"Previous Testing Accuracy : {test_accuracy*100:.2f}%")
print(f"New Testing Accuracy      : {new_accuracy*100:.2f}%")

# Compare Performance
print("\nPerformance Comparison:")
if abs(test_accuracy - new_accuracy) < 0.02:
    print("Removing SleepHours does NOT significantly affect performance.")
elif new_accuracy > test_accuracy:
    print("Performance improved after removing SleepHours.")
else:
    print("Performance decreased after removing SleepHours.")