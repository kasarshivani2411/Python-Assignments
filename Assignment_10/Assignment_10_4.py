# A program which accepts one number and prints all even numbers till that number

def PrintEven(Value):
    for i in range(1, Value+1):
        if(i % 2 == 0):
            print(i)

    # alternate way
    # for i in range(2, Value + 1, 2):
    #     print(i)


def main():
    No = int(input("Enter number : "))

    PrintEven(No)

if __name__ == "__main__":
    main()