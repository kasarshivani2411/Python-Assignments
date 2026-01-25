# A program which accept number from user and print that number of * on screen

def Display(No):
    for i in range(No):
        print("*", end=" ")

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()