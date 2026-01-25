# A program which accept number from user and display below pattern
# input : 5
# output :
# *   *   *   *   *
# *   *   *   *   
# *   *   *   
# *   *   
# *   

def Display(No):
    for i in range(No):
        for j in range(No):
            if(i <= j):
                print("*", end=" ")
        print()

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()