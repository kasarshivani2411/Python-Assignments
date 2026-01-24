# A lambda function which accepts one number and returns square of that number

Square = lambda No : No ** 2

def main():

    Value = int(input(("Enter the number : ")))

    Ret = Square(Value)
    print("Square of a number is :", Ret)

if __name__ == "__main__":
    main()