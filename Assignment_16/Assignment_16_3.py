# A program which contains one function named as Add() which accepts two numbers from user and returns addition of that two numbers

def Add(Value1, Value2):
    Ans = Value1 + Value2
    return Ans

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Add(No1, No2)
    print("Addition is :", Ret)

if __name__ == "__main__":
    main()