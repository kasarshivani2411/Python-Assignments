# A program which accepts one number and print its factors

def Factors(Value):
    for i in range(1, Value+1):
        if(Value % i == 0):
            print(i)
        

def main():
    No = int(input("Enter number : "))

    Factors(No)

if __name__ == "__main__":
    main()