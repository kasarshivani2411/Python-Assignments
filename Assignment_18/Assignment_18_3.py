# A program which accepts N numbers from user and store it into a list. Return minimum number from that list

def Minimum(Values):
    iMin = Values[0]

    for i in Values:
        if(i < iMin):
            iMin = i

    return iMin

def main():
    Size = 0
    Data = list()

    Size = int(input("Number of elements : "))

    print("Input elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)              # Data[i] = Value

    Ret = Minimum(Data)
    print("Minimum number from list :", Ret)

if __name__ == "__main__":
    main()