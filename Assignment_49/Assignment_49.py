import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# --------------------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------------------
df = pd.read_csv("diabetes.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())

# --------------------------------------------------------------
# 2. EDA
# --------------------------------------------------------------
sns.countplot(x='Outcome', data=df)
plt.title("Distribution of Diabetes Outcome")
plt.show()

df.hist(figsize=(10,10))
plt.show()

plt.figure(figsize=(12,8))
sns.boxplot(data=df)
plt.xticks(rotation=90)
plt.show()

# --------------------------------------------------------------
# 3. Data Preprocessing
# --------------------------------------------------------------

# Columns where 0 is invalid
zero_value_columns = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for col in zero_value_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    
    median = df[col].median()
    
    # Replace 0 with median
    df[col] = df[col].replace(0, median)
    
    # Replace NaN with median
    df[col] = df[col].fillna(median)

print("\nAfter preprocessing:")
print(df[zero_value_columns].head())

# --------------------------------------------------------------
# 4. Split Data
# --------------------------------------------------------------
X = df.drop('Outcome', axis=1)
Y = df['Outcome']

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

# --------------------------------------------------------------
# 5. Train Models
# --------------------------------------------------------------
model_lr = LogisticRegression(max_iter=5000)
model_dt = DecisionTreeClassifier(random_state=42)
model_knn = KNeighborsClassifier(n_neighbors=5)

model_lr.fit(X_train, Y_train)
model_dt.fit(X_train, Y_train)
model_knn.fit(X_train, Y_train)

# --------------------------------------------------------------
# 6. Predictions
# --------------------------------------------------------------
pred_lr = model_lr.predict(X_test)
pred_dt = model_dt.predict(X_test)
pred_knn = model_knn.predict(X_test)

# --------------------------------------------------------------
# 7. Evaluation Function
# --------------------------------------------------------------
def evaluate(y_true, y_pred, name):
    print(f"\n {name}")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
    print("Classification Report:\n", classification_report(y_true, y_pred))

evaluate(Y_test, pred_lr, "Logistic Regression")
evaluate(Y_test, pred_dt, "Decision Tree")
evaluate(Y_test, pred_knn, "KNN")

# --------------------------------------------------------------
# 8. Confusion Matrix Plot
# --------------------------------------------------------------
def plot_cm(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

plot_cm(Y_test, pred_lr, "Logistic Regression")
plot_cm(Y_test, pred_dt, "Decision Tree")
plot_cm(Y_test, pred_knn, "KNN")

# --------------------------------------------------------------
# 9. Final Prediction (Best Model)
# --------------------------------------------------------------
final_pred = pred_dt

output = pd.DataFrame({
    "Actual": Y_test.values,
    "Predicted": final_pred
})

output.to_csv("diabetes_predictions.csv", index=False)

print("\nPredictions saved successfully!")
print(output.head())