# A program which accept number from user and return its factorial

def Factorial(No):
    Fact = 1

    for i in range(No, 1, -1):
        Fact = Fact * i

    return Fact

def main():
    Value = int(input("Enter the number : "))

    Ret = Factorial(Value)
    print("Factorial is :", Ret)

if __name__ == "__main__":
    main()