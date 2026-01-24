# A lambda function which accepts one number and returns True if number is odd otherwie False

Odd = lambda No : No % 2 != 0

def main():

    Value = int(input(("Enter the number : ")))

    Ret = Odd(Value)
    if(Ret == True):
        print("Odd number")
    else:
        print("Even number")

if __name__ == "__main__":
    main()