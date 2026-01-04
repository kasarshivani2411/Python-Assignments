# Difference between function with parameters and without parameters

def Addition(Value1, Value2):                 # Function with parameter
    Ans = 0
    Ans = Value1 + Value2
    return Ans

def main():                                         # Function without parameter
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Result = 0
    Result = Addition(No1, No2)
    print("Addition is :", Result)

main()