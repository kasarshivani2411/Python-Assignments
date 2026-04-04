import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

# --------------------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------------------
df = pd.read_csv("bank-full.csv", sep=';')

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistics:")
print(df.describe())

# --------------------------------------------------------------
# 2. Handle Missing / Unknown Values
# --------------------------------------------------------------
df.replace('unknown', np.nan, inplace=True)

# Fill categorical missing values with mode
for col in df.select_dtypes(include=['object', 'string']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# --------------------------------------------------------------
# 3. Target Variable Distribution
# --------------------------------------------------------------
sns.countplot(x='y', data=df)
plt.title("Target Distribution")
plt.show()

# --------------------------------------------------------------
# 4. Encoding Categorical Variables
# --------------------------------------------------------------
df = pd.get_dummies(df, drop_first=True)

# --------------------------------------------------------------
# 5. Split Features & Target
# --------------------------------------------------------------
X = df.drop('y_yes', axis=1)
Y = df['y_yes']

# --------------------------------------------------------------
# 6. Feature Scaling
# --------------------------------------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --------------------------------------------------------------
# 7. Train-Test Split
# --------------------------------------------------------------
X_train, X_test, Y_train, Y_test = train_test_split(
    X_scaled, Y, test_size=0.2, random_state=42
)

# --------------------------------------------------------------
# 8. Train Models
# --------------------------------------------------------------
lr = LogisticRegression(max_iter=5000)
knn = KNeighborsClassifier(n_neighbors=5)
rf = RandomForestClassifier(n_estimators=100, random_state=42)

lr.fit(X_train, Y_train)
knn.fit(X_train, Y_train)
rf.fit(X_train, Y_train)

# --------------------------------------------------------------
# 9. Evaluation Function
# --------------------------------------------------------------
def evaluate_model(model, X_test, Y_test, name):
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:,1]

    print(f"\n🔹 {name}")
    print("Accuracy:", accuracy_score(Y_test, y_pred))
    print("ROC-AUC:", roc_auc_score(Y_test, y_prob))
    print("Confusion Matrix:\n", confusion_matrix(Y_test, y_pred))
    print("Classification Report:\n", classification_report(Y_test, y_pred))

    return y_pred, y_prob

# Evaluate all models
pred_lr, prob_lr = evaluate_model(lr, X_test, Y_test, "Logistic Regression")
pred_knn, prob_knn = evaluate_model(knn, X_test, Y_test, "KNN")
pred_rf, prob_rf = evaluate_model(rf, X_test, Y_test, "Random Forest")

# --------------------------------------------------------------
# 10. Confusion Matrix Plot
# --------------------------------------------------------------
def plot_cm(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

plot_cm(Y_test, pred_lr, "Logistic Regression")
plot_cm(Y_test, pred_knn, "KNN")
plot_cm(Y_test, pred_rf, "Random Forest")

# --------------------------------------------------------------
# 11. ROC Curve
# --------------------------------------------------------------
def plot_roc(y_test, prob, label):
    fpr, tpr, _ = roc_curve(y_test, prob)
    plt.plot(fpr, tpr, label=label)

plt.figure(figsize=(8,6))

plot_roc(Y_test, prob_lr, "Logistic Regression")
plot_roc(Y_test, prob_knn, "KNN")
plot_roc(Y_test, prob_rf, "Random Forest")

plt.plot([0,1],[0,1],'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()

# --------------------------------------------------------------
# 12. Save Predictions (Final Output)
# --------------------------------------------------------------
final_predictions = pred_rf 

output = pd.DataFrame({
    "Actual": Y_test.values,
    "Predicted": final_predictions
})

output.to_csv("bank_predictions.csv", index=False)

print("\nPredictions saved to bank_predictions.csv")
print(output.head())