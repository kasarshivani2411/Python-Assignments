# A lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5

Divisible = lambda No : (No % 3 == 0) and (No % 5 == 0)

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter number of elements you want : "))

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)             

    FData = list(filter(Divisible, Data))
    print("Numbers which are divisible by both 3 and 5 after filter are :", FData)

if __name__ == "__main__":
    main()