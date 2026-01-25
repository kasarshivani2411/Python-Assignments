# A program which accepts N numbers from user and store it into a list. Accept one another number from user and return frequency of that number from List

def Frequency(Values, Num):
    Count = 0

    for i in Values:
        if(i == Num):
            Count = Count + 1

    return Count

def main():
    Size = 0
    Data = list()
    No = 0

    Size = int(input("Number of elements : "))

    print("Input elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    No = int(input("Element to search : "))

    Ret = Frequency(Data, No)
    print("Frequency of number from list :", Ret)

if __name__ == "__main__":
    main()