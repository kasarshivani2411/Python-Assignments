# A program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even Number" otherwise display "Odd Number" on console

def ChkNum(Value):
    return Value % 2 == 0

def main():
    No = int(input("Enter the number : "))

    Ret = ChkNum(No)
    if(Ret == True):
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()