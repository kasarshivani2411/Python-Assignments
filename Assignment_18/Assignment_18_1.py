# A program which accepts N numbers from user and store it into a list. Return addition of all elements in that list

def Addition(Values):
    Sum = 0

    for i in Values:
        Sum = Sum + i

    return Sum

def main():
    Size = 0
    Data = list()

    Size = int(input("Number of elements : "))

    print("Input elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)              # Data[i] = Value

    Ret = Addition(Data)
    print("Addition of all elements is :", Ret)

if __name__ == "__main__":
    main()