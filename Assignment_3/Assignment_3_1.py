# A function to accept two numbers and return their multiplication
# User defined functions

def Multiplication(Value1, Value2):
    Ans = 0
    Ans = Value1 * Value2
    return Ans

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Result = 0
    Result = Multiplication(No1, No2)
    print("Multiplication is :", Result)

main()