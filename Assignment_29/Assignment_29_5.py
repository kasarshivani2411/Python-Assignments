# Frequency of a String in File
# Problem Statement : Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.
# Input : Demo.txt Marvellous
# Expected Output : Count how many times "Marvellous" appears in Demo.txt.

import os

def FindTerm(fName, term):
    Count = 0

    if(not os.path.exists(fName)):
        print(f"{fName} does not exists in the directory")

    fobj = open(fName, "r")

    Data = fobj.read()
    Count = Data.count(term)

    fobj.close()

    return Count

def main():
    FileName = input("Enter the file name : ")
    Value = input("Enter the search term : ")

    Ret = FindTerm(FileName, Value)
    print(f"{Ret} time/s {Value} appears in {FileName}")

if __name__ == "__main__":
    main()