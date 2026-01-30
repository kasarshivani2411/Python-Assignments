# Write a python program to implement a class named Numbers with the following specifications:
# The class should contain one instance variable:
    # Value
# Define a constructor (__init__) that accepts a number from user and initializes Value.
# Implement following instance methods:
    # ChkPrime() - returns True is the number is Prime, otherwise return False
    # ChkPerfect() - returns True is the number is Perfect, otherwise return False
    # Factors() - displays all factors of the number
    # SumFactors() - returns the sum of all factors
        # (You may use this method as a helper in ChkPerfect() if required)

# Create multiple objects and call all methods.

class Numbers:
    def __init__(self, Num):
        self.Value = Num

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print(f"Factors of {self.Value} are:", end=" ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        Sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i
        return Sum

    def ChkPerfect(self):
        return self.SumFactors() == self.Value


def main():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    No1 = Numbers(n1)
    print("Number :", No1.Value)
    print("Is Prime :", No1.ChkPrime())
    print("Is Perfect :", No1.ChkPerfect())
    No1.Factors()
    print("Sum of factors is :", No1.SumFactors())

    print("\n----------------------\n")

    No2 = Numbers(n2)
    print("Number :", No2.Value)
    print("Is Prime :", No2.ChkPrime())
    print("Is Perfect :", No2.ChkPerfect())
    No2.Factors()
    print("Sum of factors is :", No2.SumFactors())


if __name__ == "__main__":
    main()