# A program which accepts one number from user and checks whether it is prime or not

def CheckPrime(Value):
    if Value <= 1:
        return False
    
    for i in range(2, Value):
        if(Value % i == 0):
            return False
    return True

def main():
    No = int(input("Enter number : "))

    Ret = CheckPrime(No)
    if(Ret == True):
        print("It is Prime Number")
    else:
        print("It is Not a Prime Number")

if __name__ == "__main__":
    main()