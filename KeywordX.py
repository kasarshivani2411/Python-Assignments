def EmployeeInfo(Name, Age, Salary, City):
    print("Name :", Name)
    print("Age :", Age)
    print("Salary :", Salary)
    print("City :", City)

def main():
    # Keyword Arguments
    EmployeeInfo(Age=25, Name="Shivani", City="Pune", Salary=None)          # Correct

if __name__ == "__main__":
    main()