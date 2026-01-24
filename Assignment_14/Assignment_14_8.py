# A lambda function which accepts two numbers and returns the addition

Addition = lambda No1, No2 : No1 + No2

def main():

    Value1 = int(input(("Enter first number : ")))
    Value2 = int(input(("Enter second number : ")))

    Ret = Addition(Value1, Value2)
    print("Addition of numbers is :", Ret)

if __name__ == "__main__":
    main()