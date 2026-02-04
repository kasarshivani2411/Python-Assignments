# Search a word in a  File
# Problem Statement : Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
# Input : Demo.txt Marvellous
# Expected Output : Display whether the word Marvellous is found in Demo.txt or not.

import os

def ChkWord(fName, word):
    if(not os.path.exists(fName)):
        print("File does not exists")
        return
    
    fobj = open(fName, "r")

    Data = fobj.read()
    if word in Data:
        print(f'The word "{word}" is found in {fName}')
    else:
        print(f'The word "{word}" is not found in {fName}')
    

def main():
    FileName = input("Enter the file name : ")
    Value = input("Enter the word you want to find : ")

    ChkWord(FileName, Value)

if __name__ == "__main__":
    main()