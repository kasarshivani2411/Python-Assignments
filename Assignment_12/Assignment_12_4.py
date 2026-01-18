# A program which accepts one number and print that many numbers starting from 1

def Display(Value):
    for i in range(1, Value+1):
        print(i)
        

def main():
    No = int(input("Enter number : "))

    Display(No)

if __name__ == "__main__":
    main()


# def Display(Value):
#     return list(range(1, Value + 1))


# def main():
#     No = int(input("Enter number : "))

#     result = Display(No)
#     for i in result:
#         print(i)


# if __name__ == "__main__":
#     main()