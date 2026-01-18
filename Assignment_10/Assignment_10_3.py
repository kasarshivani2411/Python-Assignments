# A program which accepts one number and prints factorial of that number

def Factorial(Value):
    fact = 1
    for i in range(1, Value+1):             # range(2, Value+1)
        fact = fact * i

    return fact

def main():
    Ret = 0
    No = int(input("Enter number : "))

    Ret = Factorial(No)
    print("Factorial is :", Ret)

if __name__ == "__main__":
    main()