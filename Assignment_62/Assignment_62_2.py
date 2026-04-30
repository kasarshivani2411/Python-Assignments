# Write a Python program to demonstrate ReLU and Max Pooling

# Tasks:
# 1. Create a feature map with positive and negative values
# 2. Apply ReLU
# 3. Apply 2x2 max pooling
# 4. Display output after each step
# 5. Explain why pooling reduces size

# Input Feature Map

# feature_map = [
#     [ 3,  3,  3],
#     [ 0,  0,  0],
#     [-3, -3, -3]
# ]

# ReLU Rule

# If value < 0, convert it to 0
# If value >= 0, keep it same

# Expected Output

# relu_output = [
#     [3, 3, 3],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# ---------------------------------------------------------
# Program : Demonstration of ReLU and Max Pooling
# Author  : Shivani Rajendra Kasar
# ---------------------------------------------------------

import numpy as np

# ------------------------------------------------------------
# Step 1: Input Feature Map
# ------------------------------------------------------------
feature_map = np.array([
    [ 3,  3,  3],
    [ 0,  0,  0],
    [-3, -3, -3]
])

print("\nOriginal Feature Map:")
print(feature_map)

# ------------------------------------------------------------
# Step 2: Apply ReLU
# ------------------------------------------------------------
relu_output = np.maximum(0, feature_map)

print("\nAfter ReLU:")
print(relu_output)

# ------------------------------------------------------------
# Step 3: Apply 2x2 Max Pooling
# ------------------------------------------------------------
print("\n--- Max Pooling Steps ---\n")

pool_size = 2
stride = 1

output_rows = relu_output.shape[0] - pool_size + 1
output_cols = relu_output.shape[1] - pool_size + 1

pooling_output = np.zeros((output_rows, output_cols))

for i in range(output_rows):
    for j in range(output_cols):

        region = relu_output[i:i+pool_size, j:j+pool_size]

        print(f"Region [{i},{j}]:")
        print(region)

        max_val = np.max(region)

        print("Max Value:", max_val)
        print("-" * 30)

        pooling_output[i][j] = max_val

# ------------------------------------------------------------
# Step 4: Final Output
# ------------------------------------------------------------
print("\nFinal Output after Max Pooling:")
print(pooling_output)

# ------------------------------------------------------------
# Step 5: Explain why pooling reduces size
# ------------------------------------------------------------
# Pooling reduces size because it replaces a group of values with a single representative value which is maximum from the pooling matrix