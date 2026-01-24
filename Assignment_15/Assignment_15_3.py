# A lambda function using filter() which accepts a list of numbers and returns a list of odd numbers

Odd = lambda No : No % 2 != 0

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter number of elements you want : "))

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)             

    FData = list(filter(Odd, Data))
    print("Odd numbers after filter are :", FData)

if __name__ == "__main__":
    main()