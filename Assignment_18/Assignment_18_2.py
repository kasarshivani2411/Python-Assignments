# A program which accepts N numbers from user and store it into a list. Return maximum number from that list

def Maximum(Values):
    iMax = Values[0]

    for i in Values:
        if(i > iMax):
            iMax = i

    return iMax

def main():
    Size = 0
    Data = list()

    Size = int(input("Number of elements : "))

    print("Input elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)              # Data[i] = Value

    Ret = Maximum(Data)
    print("Maximum number from list :", Ret)

if __name__ == "__main__":
    main()