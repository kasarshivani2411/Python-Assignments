def EmployeeInfo(Name, Age, Salary, City):
    print("Name :", Name)
    print("Age :", Age)
    print("Salary :", Salary)
    print("City :", City)

def main():
    # Positional Arguments
    # EmployeeInfo("Shivani", 25, 2000.50, "Pune")        # Correct
    # EmployeeInfo(25, "Shivani", "Pune", 2000.50)        # Wrong

    # Keyword Arguments
    EmployeeInfo(Age=25, Name="Shivani", City="Pune", Salary=2000.50)       # Correct

if __name__ == "__main__":
    main()