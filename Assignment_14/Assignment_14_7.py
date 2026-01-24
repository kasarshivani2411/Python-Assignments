# A lambda function which accepts one number and returns True if divisible by 5

Divisible = lambda No : No % 5 == 0

def main():

    Value = int(input(("Enter the number : ")))

    Ret = Divisible(Value)
    if(Ret == True):
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

if __name__ == "__main__":
    main()