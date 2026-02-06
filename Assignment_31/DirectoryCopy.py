# Design automation script which accept two directory names. Copy all files from first file directory into the second directory. Second directory should be created at run time.
    # Usage : DirectoryCopy.py "Demo" "Temp"
# Demo is name of directory which is existing and contains files in it. We have to create new Directory Temp and copy all files from Demo to temp.

import sys
import os
import shutil

def DirectoryCopy(SrcDir, DestDir):
    Ret = False

    Ret = os.path.exists(SrcDir)
    if(Ret == False):
        print("Source directory does not exist")
        return
    
    Ret = os.path.isdir(SrcDir)
    if(Ret == False):
        print("It is not a directory")
        return

    Ret = os.path.exists(DestDir)
    if(Ret == False):
        os.mkdir(DestDir)
        print(f"Directory '{DestDir}' created successfully")

    print(f"Copying files from '{SrcDir}' to '{DestDir}': ")

    for FolderName, SubFolderName, FileName in os.walk(SrcDir):
        relPath = os.path.relpath(FolderName, SrcDir)
        destFolder = os.path.join(DestDir, relPath)

        if not os.path.exists(destFolder):
            os.mkdir(destFolder)

        for file in FileName:
            srcPath = os.path.join(FolderName, file)
            destPath = os.path.join(destFolder, file)

            shutil.copy(srcPath, destPath)
            print(f"Copied : {srcPath} --> {destPath}")

def main():
    Border = "-" * 51
    print(Border)
    print("--------- Marvellous Directory Automation ---------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Usage : ScriptName DirectoryName1 DirectoryName2")
        return

    DirectoryCopy(sys.argv[1], sys.argv[2])

    print(Border)
    print("--------- Marvellous Directory Automation ---------")
    print(Border)

if __name__ == "__main__":
    main()