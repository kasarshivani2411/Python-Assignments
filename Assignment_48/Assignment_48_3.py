# Write a Python program using StandardScaler to perform feature scaling on the following dataset:
# [[25, 20000], [30, 40000], [35, 80000]]
# Print the scaled dataset

from sklearn.preprocessing import StandardScaler

def main():
    Dataset = [[25, 20000], [30, 40000], [35, 80000]]

    print("Original Dataset:")
    print(Dataset)

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(Dataset)

    print("Scaled Dataset:")
    print(scaled_data)

if __name__ == "__main__":
    main()