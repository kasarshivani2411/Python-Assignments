import Arithmetic

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Arithmetic.Add(No1, No2)
    print("Addition is :", Ret)

    Ret = Arithmetic.Sub(No1, No2)
    print("Substraction is :", Ret)

    Ret = Arithmetic.Mult(No1, No2)
    print("Multiplication is :", Ret)

    Ret = Arithmetic.Div(No1, No2)
    print("Division is :", Ret)

if __name__ == "__main__":
    main()