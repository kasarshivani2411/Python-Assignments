# A program which accepts one number and checks whether it is prime or not

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
        print("Prime number")
    else:
        print("Not a Prime number")

if __name__ == "__main__":
    main()