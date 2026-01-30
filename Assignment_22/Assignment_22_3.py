# Write a python program to implement a class named Arithmetic with the following characteristics:
# The class should contain two instance variables: Value1 and Value2.
# Define a constructor (__init__) that initializes all instance variables to 0.
# Implement the following instance methods :
    # Accept() - accepts values for Value1 and Value2 from the user.
    # Addition() - returns the addition of Value1 and Value2.
    # Substraction() - returns the substraction of Value1 and Value2.
    # Multiplication() - returns the multiplication of Value1 and Value2.
    # Division() - returns the division of Value1 and Value2 (handle division by 0 properly).
# Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the first value : "))
        self.Value2 = int(input("Enter the second value : "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if(self.Value2 == 0):
            return "Divisible by 0 is not allowed"
        else:
            return self.Value1 / self.Value2
def main():
    obj1 = Arithmetic()
    obj2 = Arithmetic()

    print("Arithmetic operations with obj1")
    obj1.Accept()
    print("Addition is :", obj1.Addition())
    print("Substraction is :", obj1.Substraction())
    print("Multiplication is :", obj1.Multiplication())
    print("Division is :", obj1.Division())

    print("Arithmetic operations with obj2")
    obj2.Accept()
    print("Addition is :", obj2.Addition())
    print("Substraction is :", obj2.Substraction())
    print("Multiplication is :", obj2.Multiplication())
    print("Division is :", obj2.Division())

if __name__ == "__main__":
    main()