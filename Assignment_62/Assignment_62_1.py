# Write a Python program to manually perform convolution

# Input:
# A 5x5 matrix representing grayscale image

# Kernel:
# A 3x3 edge detection filter

# Tasks:
# 1. Move kernel over image
# 2. Perform multiplication and addition
# 3. Generate feature map
# 4. Print each region calculation

# image = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
#     ]  

# Kernel Matrix

# kernel = [
#     [-1, -1, -1],
#     [ 0,  0,  0],
#     [ 1,  1,  1]
# ]

# First region Calculation

# Region:
# 0   0   0
# 0   0   0
# 1   1   1

# Kernel:
# -1  -1  -1
#  0   0   0
#  1   1   1

# Calculation:
# 0*-1 + 0*-1 + 0*-1 +
# 0*0 + 0*0 + 0*0 +
# 1*1 + 1*1 + 1*1 

# Output = 3

# Expected feature Map

# feature_map = [
#     [ 3, 3, 3],
#     [ 0, 0, 0],
#     [-3,-3,-3]
# ]

# ---------------------------------------------------------
# Program : Manually performing convolution
# Author  : Shivani Rajendra Kasar
# ---------------------------------------------------------

import numpy as np

# ------------------------------------------------------------
# Step 1: Input Image (5x5)
# ------------------------------------------------------------
image = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

print("\nOriginal Image (5x5)")
print(image)

# ------------------------------------------------------------
# Step 2: Kernel (3x3 Edge Detection)
# ------------------------------------------------------------
kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])

print("\nKernel (3x3)")
print(kernel)

# ------------------------------------------------------------
# Step 3: Convolution Operation
# Output size = (5-3+1) x (5-3+1) = 3x3
# ------------------------------------------------------------
feature_map = np.zeros((3, 3))

print("\n--- Convolution Steps ---\n")

for i in range(3):
    for j in range(3):

        # Extract 3x3 region
        region = image[i:i+3, j:j+3]

        print(f"Region [{i},{j}] :")
        print(region)

        # Element-wise multiplication
        mul = region * kernel

        print("Multiplication:")
        print(mul)

        # Sum of all values
        result = np.sum(mul)

        print("Sum =", result)
        print("-" * 30)

        feature_map[i][j] = result

# ------------------------------------------------------------
# Step 4: Output Feature Map
# ------------------------------------------------------------
print("\nFinal Feature Map")
print(feature_map)