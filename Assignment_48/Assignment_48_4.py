# Write a Python program to calculate the Euclidean distance between two points
# before and after applying feature scaling and explain the differene in results.

import math

def main():
    point1 = [25, 20000]
    point2 = [35, 80000]

    distance = math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

    print("Euclidean Distance:", distance)

if __name__ == "__main__":
    main()