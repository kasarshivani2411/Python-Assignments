# Design a python application that creates three threads named Small, Capital and Digits.
# All threads should accept string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display:
    # Thread ID
    # Thread Name

import threading

def Small(Str):
    Count = 0
    for ch in Str:
        if(ch.islower()):
            Count = Count + 1

    print()
    print("Small Thread")
    print("Small Thread ID :", threading.get_ident())
    print("Small Thread Name :", threading.current_thread().name)
    print("Lowercase characters count is :", Count)

def Capital(Str):
    Count = 0
    for ch in Str:
        if(ch.isupper()):
            Count = Count + 1

    print()
    print("Capital Thread")
    print("Capital Thread ID :", threading.get_ident())
    print("Capital Thread Name :", threading.current_thread().name)
    print("Uppercase characters count is :", Count)

def Digits(Str):
    Count = 0
    for ch in Str:
        if(ch.isdigit()):
            Count = Count + 1

    print()
    print("Digits Thread")
    print("Digits Thread ID :", threading.get_ident())
    print("Digits Thread Name :", threading.current_thread().name)
    print("Uppercase characters count is :", Count)

def main():
    Value = input("Enter the string : ")

    t1 = threading.Thread(target=Small, args=(Value,))
    t2 = threading.Thread(target=Capital, args=(Value,))
    t3 = threading.Thread(target=Digits, args=(Value,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()