# Design automation script which accept directory name and two file extensions from user. Rename all files with first file extension with the second file extension.
    # Usage : DirectoryRename.py "Demo" ".txt" ".doc"
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
# After execution this script each .txt file gets renamed as .doc

import sys
import os

def DirectoryRename(DirName, FileExt1, FileExt2):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    print(f"Files with extension {FileExt1} in directory '{DirName}' replaced with {FileExt2}: ")

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for file in FileName:
            if file.endswith(FileExt1):

                oldPath = os.path.join(FolderName, file)

                newFile = file.replace(FileExt1, FileExt2)
                newPath = os.path.join(FolderName, newFile)

                os.rename(oldPath, newPath)
                print(f"{oldPath}  -->  {newPath}")

def main():
    Border = "-"*51
    print(Border)
    print("--------- Marvellous Directory Automation ---------")
    print(Border)

    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        print("Usage : ScriptName DirectoryName FileExtension1 FileExtension2")
        return

    DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

    print(Border)
    print("--------- Marvellous Directory Automation ---------")
    print(Border)    

if __name__ == "__main__":
    main()