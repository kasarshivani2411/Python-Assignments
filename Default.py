def EmployeeInfo(Name = "Shivani", Age = 25, Salary = 2000.50, City = "Pune"):
    print("Name :", Name)
    print("Age :", Age)
    print("Salary :", Salary)
    print("City :", City)

def main():
    # EmployeeInfo(Age=25, Name="Shivani", Salary=2000.50)       # Correct
    EmployeeInfo()

if __name__ == "__main__":
    main()