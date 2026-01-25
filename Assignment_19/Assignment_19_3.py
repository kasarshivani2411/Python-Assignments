# A program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from the user. Filter should filter out all such numbers which greater than or equal to 70
# and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers

from functools import reduce

def FilterElements(No):
    return (No >= 70 and No <= 90)

def Increment(No):
    return (No + 10)

def Mul(A, B):
    return A * B

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

    MData = list(map(Increment, FData))
    print("List after map :", MData)

    RData = reduce(Mul, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()