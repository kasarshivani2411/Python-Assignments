# Design a Python application where multiple threads update a shared variable
# Use lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete the execution.

import threading

iCnt = 0
lobj = threading.Lock()

def Thread1():
    global iCnt

    for _ in range(1000):
        with lobj:
            iCnt = iCnt + 1

def Thread2():
    global iCnt

    for _ in range(1000):
        with lobj:
            iCnt = iCnt + 1

def Thread3():
    global iCnt

    for _ in range(1000):
        with lobj:
            iCnt = iCnt + 1

def main():
    global iCnt

    t1 = threading.Thread(target=Thread1)
    t2 = threading.Thread(target=Thread2)
    t3 = threading.Thread(target=Thread3)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Value of iCnt is :", iCnt)

if __name__ == "__main__":
    main()