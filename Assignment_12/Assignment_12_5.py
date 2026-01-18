# A program which accepts one number and print that many numbers in reverse order

def Display(Value):
    for i in range(Value, 0, -1):
        print(i)
        

def main():
    No = int(input("Enter number : "))

    Display(No)

if __name__ == "__main__":
    main()


# def Display(Value):
#     return list(range(Value, 0, -1))


# def main():
#     No = int(input("Enter number : "))

#     result = Display(No)
#     for i in result:
#         print(i)


# if __name__ == "__main__":
#     main()