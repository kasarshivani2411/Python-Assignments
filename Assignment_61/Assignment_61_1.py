# Create a neural network model to predict whether a customer will leave a service.
# Features:
# 1. Age
# 2. Monthly Charges
# 3. Tenure
# 4. Number of complaints
# 5. Customer support calls

# X = [
#     [25, 500, 12, 1, 2],
#     [30, 700, 24, 0, 1],
#     [45, 1200, 6, 5, 8],
#     [50, 1500, 5, 6, 10],
#     [28, 600, 18, 1, 1],
#     [35, 800, 30, 0, 0],
#     [48, 1400, 4, 7, 9],
#     [52, 1600, 3, 8, 12],
#     [27, 550, 20, 0, 1],
#     [42, 1300, 8, 4, 7],
#     ]  

# y = [
#     0, 0, 1, 1, 0, 0, 1, 1, 0, 1
# ]

# Output : 
# 0 = Customer will stay
# 1 = Customer will leave

# Tasks:
# 1. Load or create dataset
# 2. Clean the dataset
# 3. Apply StandardScaler
# 4. Train FNN model
# 5. Evaluate accuracy

# Feature Meaning
# [Age, Monthly Charges, Tenure, Complaints, Support calls]

# Output Meaning
# 0 = Customer will stay
# 1 = Customer will leave

# Test Input:
# new_customer = [[46, 1450, 5, 6, 9]]

# Expected Output:
# Prediction : Customer may leave

# ---------------------------------------------------------
# Program : FNN model to predict whether a customer will leave a service
# Author  : Shivani Rajendra Kasar
# ---------------------------------------------------------

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# ------------------------------------------------------------
# Step 1: Prepare the dataset
# ------------------------------------------------------------
X = [
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7],
    ]  

y = [0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

# ------------------------------------------------------------
# Step 2: Split dataset
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ------------------------------------------------------------
# Step 3: Scale the input data
# ------------------------------------------------------------
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ------------------------------------------------------------
# Step 4: Create FNN model
# ------------------------------------------------------------
model = MLPClassifier(
    hidden_layer_sizes=(5,),
    activation='relu',
    solver='lbfgs',
    max_iter=2000,
    random_state=42
)

# ------------------------------------------------------------
# Step 5: Train the model
# ------------------------------------------------------------
model.fit(X_train_scaled, y_train)

# ------------------------------------------------------------
# Step 6: Predict
# ------------------------------------------------------------
y_pred = model.predict(X_test_scaled)

# ------------------------------------------------------------
# Step 7: Evaluate
# ------------------------------------------------------------
print("Actual Output   :", y_test)
print("Predicted Output:", y_pred.tolist())

accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy of model:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# ------------------------------------------------------------
# Step 8: Predict new customer
# ------------------------------------------------------------
new_customer = [[46, 1450, 5, 6, 9]]
new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)

if prediction[0] == 1:
    print("\nNew Prediction : Customer may leave")
else:
    print("\nNew Prediction : Customer may stay")