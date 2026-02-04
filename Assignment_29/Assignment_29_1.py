# Check File Exists in Current Directory
# Problem Statement : Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
# Input : Demo.txt
# Expected Output : Display whether Demo.txt exists or not.

import os

def ChkFileExists(fName):
    return os.path.exists(fName)

def main():
    FileName = input("Enter the file name : ")

    Result = ChkFileExists(FileName)
    if(Result == True):
        print(f"{FileName} exist in the current directory")
    else:
        print(f"{FileName} does not exist in the current directory")

if __name__ == "__main__":
    main()