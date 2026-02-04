# Compare Two Files (Command Line)
# Problem Statement : Write a program which accepts two file names through command line arguments and compares the contents of both files.
    # If both files contain the same contents, display Success
    # Otherwise display Failure
# Input : (Command Line):
    # Demo.txt Hello.txt
# Expected Output : Success OR Failure.

import sys
import os

def CompareFileContents(fileName1, fileName2):
    fobj1 = open(fileName1, "r")
    fobj2 = open(fileName2, "r")

    Data1 = fobj1.read()
    Data2 = fobj2.read()

    if(Data1 == Data2):
        print("Success")
    else:
        print("Failure")

    fobj1.close()
    fobj2.close()

def ChkFileExists(fName1, fName2):
    if(not os.path.exists(fName1)):
        print(f"{fName1} does not exists in the directory")
    elif(not os.path.exists(fName2)):
        print(f"{fName2} does not exists in the directory")
    else:
        CompareFileContents(fName1, fName2)

def main():
    if(len(sys.argv) != 3):
        print("Invalid number of command line arguments")
        print("Usage : ApplicationName.py <FirstFileName> <SecondFileName>")
        return
    
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    ChkFileExists(FileName1, FileName2)

if __name__ == "__main__":
    main()