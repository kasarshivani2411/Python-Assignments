# Design a Python application that creates two threads
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from same list.
# Return the result to the main thread and display them.

import threading

Sum = 0
Prod = 1

def Thread1(Values):
    global Sum

    for i in Values:
        Sum = Sum + i

    return Sum

def Thread2(Values):
    global Prod

    for i in Values:
        Prod = Prod * i

    return Prod

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter the number of elements : "))
    for _ in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=Thread1, args=(Data,))
    t2 = threading.Thread(target=Thread2, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements :", Sum)
    print("Product of elements :", Prod)

if __name__ == "__main__":
    main()