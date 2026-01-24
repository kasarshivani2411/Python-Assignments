# A lambda function which accepts two numbers and returns maximum number

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2

def main():

    Value1 = int(input(("Enter first number : ")))
    Value2 = int(input(("Enter second number : ")))

    Ret = Maximum(Value1, Value2)
    print("Maximum number is :", Ret)

if __name__ == "__main__":
    main()