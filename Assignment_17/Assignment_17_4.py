# A program which accept number from user and return addition of its factors

def SumFactors(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i
    return Sum

def main():
    Value = int(input("Enter the number : "))

    Ret = SumFactors(Value)
    print("Addition of factors is :", Ret)

if __name__ == "__main__":
    main()