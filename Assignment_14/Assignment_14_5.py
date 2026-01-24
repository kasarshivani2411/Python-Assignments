# A lambda function which accepts one number and returns True if number is even otherwie False

Even = lambda No : No % 2 == 0

def main():

    Value = int(input(("Enter the number : ")))

    Ret = Even(Value)
    if(Ret == True):
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()