# Display File Contents
# Problem Statement : Write a program which accepts a file name from the user, opens that file and displays the entire contents on the console.
# Input : Demo.txt
# Expected Output : Display contents of Demo.txt on console.

import os

def DisplayFileContents(fileName):
    fobj = open(fileName, "r")

    Data = fobj.read()
    print(Data)

    fobj.close()

def ChkFileExists(fName):
    if(os.path.exists(fName)):
        DisplayFileContents(fName)
    else:
        print(f"{fName} does not exist in the current directory")

def main():
    FileName = input("Enter the file name : ")

    ChkFileExists(FileName)

if __name__ == "__main__":
    main()