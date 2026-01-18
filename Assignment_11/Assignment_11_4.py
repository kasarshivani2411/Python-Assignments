# A program which accepts one number and prints the reverse of that number

def ReverseNumber(Value):
    Digit = 0
    ReverseNo = 0

    while(Value != 0):
        Digit = Value % 10
        ReverseNo = ReverseNo * 10 + Digit
        Value = Value//10               
    return ReverseNo
        

def main():
    No = int(input("Enter number : "))

    Ret = ReverseNumber(No)
    print("Reversed number is :", Ret)

if __name__ == "__main__":
    main()