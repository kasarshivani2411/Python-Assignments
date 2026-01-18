# A program which accepts one number and prints square of that number

def CalculateSquare(Value):
    return Value * Value

def main():
    Ret = 0
    No = int(input("Enter number : "))

    Ret = CalculateSquare(No)
    print(Ret)

if __name__ == "__main__":
    main()