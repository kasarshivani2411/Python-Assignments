# Design automation script which accept directory name and file extension from user. Display all files with that extension.
    # Usage : DirectoryFileSearch.py "Demo" ".txt"
# Demo is name of directory and .txt is the extension that we want to search.

import sys
import os

def DisplayFileNames(DirName, FileExt):
    Ret = False
    Found = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for file in FileName:
            if file.endswith(FileExt):
                if(not Found):
                    print(f"Files with extension {FileExt} in directory '{DirName}' are :")
                    Found = True
                fullPath = os.path.join(FolderName, file)
                print(fullPath)

    if(not Found):
        print("There are no files with this extension")

def main():
    Border = "-"*51
    print(Border)
    print("--------- Marvellous Directory Automation ---------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Usage : ScriptName DirectoryName FileExtension")
        return

    DisplayFileNames(sys.argv[1], sys.argv[2])

    print(Border)
    print("--------- Marvellous Directory Automation ---------")
    print(Border)    

if __name__ == "__main__":
    main()