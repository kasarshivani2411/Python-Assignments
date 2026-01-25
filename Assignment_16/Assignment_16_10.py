# A program which accept name from user and display length of its name

def Display(Data):
    Count = 0
    # Count = len(Data)
    for i in Data:
        Count = Count + 1
    return Count

def main():
    Value = input("Enter the name : ")

    Ret = Display(Value)
    print("Count is :", Ret)

if __name__ == "__main__":
    main()