# A lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5

StringsLen = lambda str : len(str) > 5

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter number of strings you want : "))

    print("Enter the elements : ")
    for i in range(Size):
        Value = input()
        Data.append(Value)             

    FData = list(filter(StringsLen, Data))
    print("Strings having length greater than 5 are :", FData)

if __name__ == "__main__":
    main()