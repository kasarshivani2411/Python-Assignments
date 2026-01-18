# A program which accepts one number and prints cube of that number

def CalculateCube(Value):
    return Value * Value * Value

def main():
    Ret = 0
    No = int(input("Enter number : "))

    Ret = CalculateCube(No)
    print(Ret)

if __name__ == "__main__":
    main()