# A program which accepts number from user and check whether that number is positive or negative or zero

def ChkNum(No):
    if No > 0:
        print("Positive Number")
    elif No < 0:
        print("Negative number")
    elif No == 0:
        print("Zero")

def main():
    Value = int(input("Enter the number : "))

    ChkNum(Value)

if __name__ == "__main__":
    main()