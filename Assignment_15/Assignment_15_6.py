# A lambda function using reduce() which accepts a list of numbers and returns the minumum element

from functools import reduce

Minimum = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter number of elements you want : "))

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)             

    RData = reduce(Minimum, Data)
    print("Minimum from all numbers is :", RData)

if __name__ == "__main__":
    main()