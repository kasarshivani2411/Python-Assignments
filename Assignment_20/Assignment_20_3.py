# Design a python application that creates two threads named EvenList and OddList.
# Both threads should accept list of integers as input
# The EvenList thread should : 
    # Extract all even elements from the list.
    # Calculate and display their sum.
# The OddFactor thread should : 
    # Extract all odd elements from the list.
    # Calculate and display their sum.
# Thread should run concurrently

import threading

def EvenList(Values):
    Sum = 0
    for i in Values:
        if(i % 2 == 0):
            Sum = Sum + i

    print("Sum of all even elements is :", Sum)
    

def OddList(Values):
    Sum = 0
    for i in Values:
        if(i % 2 != 0):
            Sum = Sum + i

    print("Sum of all odd elements is :", Sum)

def main():
    Size = 0
    Data = list()

    Size = int(input("Number of elements : "))

    print("Input elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=EvenList, args=(Data,))
    t2 = threading.Thread(target=OddList, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()