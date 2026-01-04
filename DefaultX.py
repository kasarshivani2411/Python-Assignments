def EmployeeInfo(Name, Age, Salary, City = "Mumbai"):
    print("Name :", Name)
    print("Age :", Age)
    print("Salary :", Salary)
    print("City :", City)

def main():
    EmployeeInfo("Shivani", 25, 2000.50)
    EmployeeInfo("Shivani", 25, 2000.50, "Pune")

if __name__ == "__main__":
    main()