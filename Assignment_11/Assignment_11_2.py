# A program which accepts one number and prints the count of digits in that number

def CountDigits(Value):
    Count = 0
    while(Value != 0):
        Count = Count + 1
        Value = Value//10               # single slash gives answer in floating point number, for integer we need to give // here 
    return Count
        

def main():
    No = int(input("Enter number : "))

    Ret = CountDigits(No)
    print("Count of digits in a number is :", Ret)

if __name__ == "__main__":
    main()