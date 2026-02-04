# Count Words in a File
# Problem Statement : Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input : Demo.txt
# Expected Output : Total number of words in Demo.txt.

import os

def CountWords(fName):
    if(not os.path.exists(fName)):
        print("File does not exists")
        return
    
    fobj = open(fName, "r")

    Data = fobj.read()

    Count = len(Data.split())

    fobj.close()

    return Count


def main():
    FileName = input("Enter the file name : ")

    Result = CountWords(FileName)
    print(f"Total number of words in {FileName} : {Result}")

if __name__ == "__main__":
    main()