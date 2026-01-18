# A program which accepts one number and prints multiplication table of that number

def CalculateTable(Value):
    for i in range(1, 11):
        print(Value * i)

def main():
    No = int(input("Enter number : "))

    CalculateTable(No)

if __name__ == "__main__":
    main()