# A program which accept number from user and return number of digits in that number

def DigitCount(No):
    Count = 0

    while(No != 0):
        Count = Count + 1
        No = No // 10

    return Count

def main():
    Value = int(input("Enter the number : "))

    Ret = DigitCount(Value)
    print("Number of digits in a number :", Ret)

if __name__ == "__main__":
    main()