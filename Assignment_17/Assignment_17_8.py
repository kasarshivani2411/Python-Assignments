# A program which accept number from user and display below pattern
# input : 5
# output :
# 1   
# 1   2   
# 1   2   3   
# 1   2   3   4   
# 1   2   3   4   5

def Display(No):
    for i in range(No+1):
        for j in range(1, No+1):
            if(i >= j):
                print(j, end=" ")
        print()

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()