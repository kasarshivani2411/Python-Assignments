# A lambda function using filter() which accepts a list of numbers and returns count of even numbers

Divisible = lambda No : No % 2 == 0

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter number of elements you want : "))

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)             

    FData = list(filter(Divisible, Data))
    print("Even numbers after filter are :", FData)

    Count = len(FData)
    print("Count of even numbers after filter is :", Count)
    

if __name__ == "__main__":
    main()