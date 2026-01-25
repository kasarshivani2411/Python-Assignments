# A program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from the user. Filter should filter out all such numbers which are even
# Map function will calculate its square. Reduce will return addition of all that numbers

from functools import reduce

def FilterElements(No):
    return (No % 2 == 0)

def CalcSquare(No):
    return (No ** 2)

def Mul(A, B):
    return A + B

def main():
    Size = 0
    Data = list()

    Size = int(input("Number of elements : "))

    print("Input elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(FilterElements, Data))
    print("List after filter :", FData)            

    MData = list(map(CalcSquare, FData))
    print("List after map :", MData)

    RData = reduce(Mul, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()