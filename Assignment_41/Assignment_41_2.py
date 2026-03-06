# The value of K plays an important role in the KNN algorithm.
# Write a Python program that demonstrates how prediction changes when K changes.

# Dataset
    # Use the same dataset as Assignment 1.

# Point [A, B, C, D]
# X     [1, 2, 3, 6]
# Y     [2, 3, 1, 5]
# Label [R, R, B, B]

# Tasks
    # Predict the class of the same new point using:
        # K = 1
        # K = 3
        # K = 5

# Expected Output
    # Prediction Results
        # K = 1 --> Red
        # K = 3 --> Red
        # K = 5 --> Blue

import math

def EuclideanDistance(P1, P2):
    Ans = math.sqrt(((P1['X'] - P2['X']) ** 2) + ((P1['Y'] - P2['Y']) ** 2))

    return Ans

def MarvellousKNeighborsClassifier(X, Y, K):
    Border = "-"*80

    data = [
                {'point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
                {'point' : 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
                {'point' : 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
                {'point' : 'D', 'X' : 6, 'Y' : 5, 'label' : 'Blue'}
           ]
    
    print(Border)
    print("Marvellous User Defined KNN")
    print(Border)

    if K > len(data):
        print("Invalid K value")
        return

    print(Border)
    print("Training Dataset")
    print(Border)

    for i in data:
        print(i)

    print(Border)

    new_point = {'X' : X, 'Y' : Y}

    # Calculate all distances
    for d in data:
        d['distance'] = EuclideanDistance(d, new_point)

    print(Border)
    print("Calculated distances are : ")
    print(Border)

    for d in data:
        print(d)

    sorted_data = sorted(data, key=lambda item : item['distance'])

    print(Border)
    print("Sorted data is : ")
    print(Border)

    for d in sorted_data:
        print(d)

    nearest = sorted_data[:K]
    print(Border)
    print(f"Nearest {K} elements are : ")
    print(Border)
    
    for d in nearest:
        print(d)

    # Voting
    votes = {}
    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label,0) + 1

    print(Border)
    print("Voting result is : ")
    print(Border)

    for d in votes:
        print("Name :", d, ";" ,"Number of votes :", votes[d])

    print(Border)

    predicted_class = max(votes, key=votes.get)

    print(f"Predicted class of ({X}, {Y}) is :", predicted_class)

def main():
    input_X = int(input("Enter X coordinate of new point : "))
    input_Y = int(input("Enter Y coordinate of new point : "))
    input_K = int(input("Enter value of K : "))

    MarvellousKNeighborsClassifier(input_X, input_Y, input_K)

if __name__ == "__main__":
    main()