# Design a python application that creates two separate threads named Even and Odd.
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.

import threading

def Even():
    print("Even thread")
    for i in range(1, 11):
        print(i * 2, end=" ")

    print()

def Odd():
    print("Odd thread")
    for i in range(10):
        print(2 * i + 1, end=" ")

    print()

def main():
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()