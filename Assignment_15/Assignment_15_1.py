# A lambda function using map() which accepts a list of numbers and returns a list of squares of each number

Square = lambda No : No ** 2

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter number of elements you want : "))

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)              # Data[i] = Value

    MData = list(map(Square, Data))
    print("Squares of each number after map are :", MData)

if __name__ == "__main__":
    main()