# A program which accept number from user and return addition of digits in that number

def DigitAddition(No):
    Digit = 0
    Sum = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    Value = int(input("Enter the number : "))

    Ret = DigitAddition(Value)
    print("Addition of digits in a number :", Ret)

if __name__ == "__main__":
    main()