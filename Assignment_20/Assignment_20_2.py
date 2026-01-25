# Design a python application that creates two separate threads named EvenFactor and OddFactor.
# Both threads should accept one integer number as a parameter
# The EvenFactor thread should : 
    # Identify all even factors of the given number.
    # Calculate and display the sum of even factors.
# The OddFactor thread should : 
    # Identify all odd factors of the given number.
    # Calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display the message: "Exit from main" 

import threading

def EvenFactor(Num):
    Sum = 0
    print("Even Factor thread")
    for i in range(1, Num):
        if Num % i == 0 and i % 2 == 0:
            Sum = Sum + i
    
    print("Even Factors Sum is :", Sum)

def OddFactor(Num):
    Sum = 0
    print("Odd Factor thread")
    for i in range(1, Num):
        if Num % i == 0 and i % 2 != 0:
            Sum = Sum + i
    
    print("Odd Factors Sum is :", Sum)

def main():
    No = int(input("Enter the number : "))
    t1 = threading.Thread(target=EvenFactor, args=(No,))
    t2 = threading.Thread(target=OddFactor, args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()