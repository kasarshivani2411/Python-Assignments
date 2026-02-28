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

# 6. Train three Decision Tree Models with:
#     a. max_depth = 1
#     b. max_depth = 3
#     c. max_depth = None
# Compare their testing accuracies and write your observations.

# 7. Use the trained model to predict result for a student with:
#     a. StudyHours = 6
#     b. Attendance = 85
#     c. PreviousScore = 66
#     d. AssignmentsCompleted = 7
#     e. SleepHours = 7
# Will the student Pass or Fail?

# 8. Write a single structured Python program that performs:
#     1. Dataset loading
#     2. Data analysis
#     3. Visualization
#     4. Train-test split
#     5. Model training
#     6. Prediction
#     7. Accuracy calculation
#     8. Confusion matrix generation
#     9. Final conclusion

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

# Scatter plot

plt.figure(figsize=(7, 5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label= sp)

plt.title("Iris : Petal length VS Petal Width")
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

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