# A program which contains one function ChkGreater() that accepts two numbers and prints the greater number

def ChkGreater(Value1, Value2):
    if(Value1 > Value2):
        return Value1
    else:
        return Value2    

def main():
    Ret = 0
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = ChkGreater(No1, No2)
    print(Ret, "is greater")

if __name__ == "__main__":
    main()


# using built in function

# def ChkGreater(Value1, Value2):
#     return max(Value1, Value2)