# A program which accepts two numbers and print Addition, Substraction, Multiplication and Division

def Addition(Value1, Value2):
    return Value1 + Value2

def Substraction(Value1, Value2):
    return Value1 - Value2

def Multiplication(Value1, Value2):
    return Value1 * Value2

def Division(Value1, Value2):
    if Value2 == 0:
        return "Division by zero not allowed"
    return Value1 / Value2

def main():
    No1 = int(input("Enter first number : "))

    No2 = int(input("Enter second number : "))

    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")

    Option = int(input("Enter the option number : "))

    if(Option == 1):
        print("Addition is :", Addition(No1, No2))
    elif(Option == 2):
        print("Substraction is :", Substraction(No1, No2))
    elif(Option == 3):
        print("Multiplication is :", Multiplication(No1, No2))
    elif(Option == 4):
        print("Division is :", Division(No1, No2))
    else:
        print("Invalid Choice")
    

if __name__ == "__main__":
    main()