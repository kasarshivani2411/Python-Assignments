# Write a python program to implement a class named Demo with the following specifications:
# The class should contain two instance variables: No1 and No2.
# The class should contain one class variable named Value.
# Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
# Implement two instance methods :
    # Fun() - displays the values of instance variables No1 and No2
    # Gun() - displays the values of instance variables No1 and No2
# Create two objects of the Demo class as follows:
# obj1 = Demo(11, 21)
# obj2 = Demo(51, 101)
# Call the instance methods in the given sequence:
# obj1.Fun()
# obj2.Fun()
# obj1.Gun()
# obj2.Gun()

class Demo:
    Value = 0

    def __init__(self, Val1, Val2):
        self.No1 = Val1
        self.No2 = Val2

    def Fun(self):
        print("Inside Fun method :", self.No1, self.No2)

    def Gun(self):
        print("Inside Gun method :", self.No1, self.No2)

def main():
    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()