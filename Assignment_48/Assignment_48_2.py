# Write a Python program that calculates the variance and standard deviation of the dataset:
# [6, 7, 8, 9, 10, 11, 12]

import numpy as np

def main():
    Dataset = [6, 7, 8, 9, 10, 11, 12]
    
    Variance = np.var(Dataset)

    StandardDeviation = np.std(Dataset)

    print("Dataset is :", Dataset)
    print("Variance of Dataset is :", Variance)
    print("Standard Deviation of Dataset is :", StandardDeviation)

if __name__ == "__main__":
    main()