# Display File Line by Line
# Problem Statement : Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
# Input : Demo.txt
# Expected Output : Display each line of Demo.txt one by one.

import os

def DisplayLines(fName):
    if(not os.path.exists(fName)):
        print("File does not exists")
        return
    
    fobj = open(fName, "r")

    Data = fobj.readlines()

    for line in Data:
        print(line, end="")


def main():
    FileName = input("Enter the file name : ")

    DisplayLines(FileName)

if __name__ == "__main__":
    main()