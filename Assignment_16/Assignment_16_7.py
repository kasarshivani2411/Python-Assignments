# A program which contains one function that accepts one number from user and returns True if number is divisible by 5 otherwise return False

def ChkDivisibility(No):
    return No % 5 == 0

def main():
    Value = int(input("Enter the number : "))

    Ret = ChkDivisibility(Value)

    if(Ret == True):
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

if __name__ == "__main__":
    main()