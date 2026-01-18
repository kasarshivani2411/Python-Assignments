# A program which accepts one number and checks whether it is perfect number or not

def ChkPerfect(Value):
    Temp = Value
    Sum = 0
    for i in range(1, Value):
        if(Value % i == 0):
            Sum = Sum + i
    
    return Temp == Sum

def main():
    No = int(input("Enter number : "))

    Ret = ChkPerfect(No)

    if(Ret == True):
        print("Perfect number")
    else:
        print("Not Perfect number")

if __name__ == "__main__":
    main()