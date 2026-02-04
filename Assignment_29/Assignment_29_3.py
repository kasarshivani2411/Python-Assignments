# Copy File Contents into a New File (Command Line)
# Problem Statement : Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.
# Input : ABC.txt
# Expected Output : Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import sys
import os

def CopyFileContents(fileName):
    fobj = open(fileName, "r")
    dest = open("Demo.txt", "w")

    dest.write(fobj.read())

    print("Contents copied successfully into Demo.txt")

    fobj.close()
    dest.close()

def ChkFileExists(fName):
    if(os.path.exists(fName)):
        CopyFileContents(fName)
    else:
        print(f"{fName} does not exist in the current directory")

def main():
    if(len(sys.argv) != 2):
        print("Invalid number of command line arguments")
        print("Usage : ApplicationName.py <ExistingFileName>")
        return
    
    FileName = sys.argv[1]

    ChkFileExists(FileName)

if __name__ == "__main__":
    main()