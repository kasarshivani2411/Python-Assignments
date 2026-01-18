# A program which accepts one number and prints sum of first N natural numbers

def SumOfNaturalNumbers(Value):
    # if(Value < 1):
    #     return 0
    
    Sum = 0

    for i in range(1, Value+1):
        Sum = Sum + i

    return Sum

def main():
    Ret = 0
    No = int(input("Enter number : "))

    Ret = SumOfNaturalNumbers(No)
    print("Sum of natural numbers is :", Ret)

if __name__ == "__main__":
    main()