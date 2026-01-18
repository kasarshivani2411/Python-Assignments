# A program which accepts one number and prints the sum of digits

def SumDigits(Value):
    Digit = 0
    Sum = 0

    while(Value != 0):
        Digit = Value % 10
        Sum = Sum + Digit
        Value = Value//10               
    return Sum
        

def main():
    No = int(input("Enter number : "))

    Ret = SumDigits(No)
    print("Sum of digits in a number is :", Ret)

if __name__ == "__main__":
    main()