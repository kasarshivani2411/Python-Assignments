# Count Lines in a File
# Problem Statement : Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input : Demo.txt
# Expected Output : Total number of lines in Demo.txt.

import os

def CountLines(fName):
    if(not os.path.exists(fName)):
        print("File does not exists")
        return
    
    fobj = open(fName, "r")

    Data = fobj.readlines()

    Count = len(Data)

    fobj.close()

    return Count


def main():
    FileName = input("Enter the file name : ")

    Result = CountLines(FileName)
    print(f"Total number of lines in {FileName} : {Result}")

if __name__ == "__main__":
    main()