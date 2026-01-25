# A program which accepts N numbers from user and store it into list. Return addition of all prime numbers from that list. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is a part of our user defined module named as MarvellousNum. Name of the function from main Python file should be ListPrime()

import MarvellousNum

def main():
    Size = 0
    Data = list()

    Size = int(input("Number of elements : "))

    print("Input elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = MarvellousNum.ListPrime(Data)
    print("Addition of prime numbers from list is :", Ret)

if __name__ == "__main__":
    main()