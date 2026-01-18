# A program which accepts one number and checks whether it is divisible by 3 and 5

def CheckDivisible(Value):
    return (Value % 3 == 0 and Value % 5 == 0)

def main():
    No = int(input("Enter number : "))

    Ret = CheckDivisible(No)

    if(Ret == True):
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")

if __name__ == "__main__":
    main()