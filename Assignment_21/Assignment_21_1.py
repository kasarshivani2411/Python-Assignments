# Design a Python application that creates two threads named Prime and Non Prime
# Both threads should accepts a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non prime numbers from the list

import threading

def IsPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def Prime(Values):
    print("Prime thread")
    for i in Values:
        if(IsPrime(i)):
            print(i, end=" ")
    print()
    

def NonPrime(Values):
    print("NonPrime thread")
    for i in Values:
        if not (IsPrime(i)):
            print(i, end=" ")

def main():
    Size = 0
    Data = list()

    Size = int(input("Number of elements : "))

    print("Input elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=Prime, args=(Data,))
    t2 = threading.Thread(target=NonPrime, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()