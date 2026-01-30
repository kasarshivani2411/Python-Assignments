# Write a python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables:
    # Name(Account holder Name)
    # Amount(Account balance)
# The class should contain one class variable:
    # ROI(Rate of interest), initialized to 10.5
# Define a constructor (__init__) that accepts Name and initial Amount.
# Implement following instance methods:
    # Display() - displays account holder name and current balance
    # Deposit() - accepts an amount from the user and adds it to balance
    # Withdraw() - accepts an amount from the user and substracts it from balance(Ensure withdrawl is allowed only if sufficient balance exists)
    # CalculateInterest() - calculates and returns interest using formula:
        # Interest = (Amount * ROI) / 100

# Create multiple objects and demonstrate all methods.

class BankAccount:
    ROI = 10.5

    def __init__(self, UserName, AccBalance):
        self.Name = UserName
        self.Amount = AccBalance

    def Display(self):
        print("Account holder name :", self.Name)
        print("Current balance is :", self.Amount)

    def Deposit(self):
        DepositAmount = float(input("Enter the amount you want to deposit : "))
        self.Amount = self.Amount + DepositAmount
        print("***Amount depositted successfully***")

    def Withdraw(self):
        WithdrawAmount = int(input("Enter the amount you want to withdraw : "))
        if(WithdrawAmount > self.Amount):
            print("***Insufficient balance***")
        else:
            self.Amount = self.Amount - WithdrawAmount
            print("***Amount debitted successfully***")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

def main():
    obj1 = BankAccount("Shivani", 500)
    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    CalcInterest = obj1.CalculateInterest()
    print("Interest on balance :", CalcInterest)
    print("Current Balance after transactions :")
    obj1.Display()

    print("-------------------------------------------")

    obj2 = BankAccount("Kajal", 1000)
    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()
    CalcInterest = obj2.CalculateInterest()
    print("Interest on balance :", CalcInterest)
    obj2.Display()

if __name__ == "__main__":
    main()