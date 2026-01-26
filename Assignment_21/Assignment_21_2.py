# Design a Python application that creates two threads
# Thread1 should calculate and display the maximum element from an list.
# Thread2 should calculate and display the minimum element from the same list.
# The list should be accepted from user

import threading

def Maximum(Values):
    print("Maximum thread")
    iMax = Values[0]
    for i in range(0, len(Values)):
        if(iMax < Values[i]):
            iMax = Values[i]
    print("Maximum element is :", iMax)
    

def Minumum(Values):
    print("Minumum thread")
    iMin = Values[0]
    for i in range(0, len(Values)):
        if(iMin > Values[i]):
            iMin = Values[i]
    print("Minimum element is :", iMin)

def main():
    Size = 0
    Data = list()

    Size = int(input("Number of elements : "))

    print("Input elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=Maximum, args=(Data,))
    t2 = threading.Thread(target=Minumum, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()