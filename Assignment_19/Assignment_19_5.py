# A program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from the user. Filter should filter out all prime numbers
# Map function will multiply each number by 2. Reduce will return maximum number from that numbers.

from functools import reduce

def FilterElements(No):
    if No <= 1:
        return False

    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False

    return True

def Modify(No):
    return (No * 2)

def Mul(A, B):
    return (A if A > B else B)

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

    MData = list(map(Modify, FData))
    print("List after map :", MData)

    RData = reduce(Mul, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()