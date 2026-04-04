import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

# --------------------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------------------
fake_df = pd.read_csv("Fake.csv")
true_df = pd.read_csv("True.csv")

# Add labels
fake_df["label"] = 0   # Fake
true_df["label"] = 1   # Real

# Combine datasets
df = pd.concat([fake_df, true_df], ignore_index=True)

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

print("Dataset shape:", df.shape)
print(df.head())

# --------------------------------------------------------------
# 2. Data Preprocessing
# --------------------------------------------------------------

# Drop null values
df = df.dropna()

# Combine title + text (best practice)
df["content"] = df["title"] + " " + df["text"]

# Features and target
X = df["content"]
Y = df["label"]

# --------------------------------------------------------------
# 3. Feature Extraction (TF-IDF)
# --------------------------------------------------------------
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

X_tfidf = vectorizer.fit_transform(X)

print("TF-IDF Shape:", X_tfidf.shape)

# --------------------------------------------------------------
# 4. Train-Test Split
# --------------------------------------------------------------
X_train, X_test, Y_train, Y_test = train_test_split(X_tfidf, Y, test_size=0.2, random_state=42)

# --------------------------------------------------------------
# 5. Train Individual Models
# --------------------------------------------------------------
model_lr = LogisticRegression(max_iter=5000)
model_dt = DecisionTreeClassifier(random_state=42)

model_lr.fit(X_train, Y_train)
model_dt.fit(X_train, Y_train)

# Predictions
pred_lr = model_lr.predict(X_test)
pred_dt = model_dt.predict(X_test)

# --------------------------------------------------------------
# 6. Voting Classifier
# --------------------------------------------------------------

# Hard Voting
hard_model = VotingClassifier(
    estimators=[
        ('lr', model_lr),
        ('dt', model_dt)
    ],
    voting='hard'
)

hard_model.fit(X_train, Y_train)
pred_hard = hard_model.predict(X_test)

# Soft Voting
soft_model = VotingClassifier(
    estimators=[
        ('lr', model_lr),
        ('dt', model_dt)
    ],
    voting='soft'
)

soft_model.fit(X_train, Y_train)
pred_soft = soft_model.predict(X_test)

# --------------------------------------------------------------
# 7. Evaluation Function
# --------------------------------------------------------------
def evaluate(y_true, y_pred, name):
    print(f"\n🔹 {name}")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
    print("Classification Report:\n", classification_report(y_true, y_pred))

# Evaluate all
evaluate(Y_test, pred_lr, "Logistic Regression")
evaluate(Y_test, pred_dt, "Decision Tree")
evaluate(Y_test, pred_hard, "Hard Voting")
evaluate(Y_test, pred_soft, "Soft Voting")

# --------------------------------------------------------------
# 8. Confusion Matrix
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
plot_cm(Y_test, pred_hard, "Hard Voting")
plot_cm(Y_test, pred_soft, "Soft Voting")

# --------------------------------------------------------------
# 9. Final Prediction Example
# --------------------------------------------------------------
sample_news = ["Breaking: Government announces new economic policy"]

sample_vector = vectorizer.transform(sample_news)

prediction = soft_model.predict(sample_vector)

print("\nSample Prediction:")
print("Fake" if prediction[0] == 0 else "Real")