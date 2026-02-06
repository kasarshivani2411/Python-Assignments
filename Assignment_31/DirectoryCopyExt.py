# Design automation script which accept two directory names and one file extension. Copy all files with the specified extension from first directory into second directory. Second directory should be created at run time.
    # Usage : DirectoryCopyExt.py "Demo" "Temp" ".exe"
# Demo is name of directory which is existing and contains files in it. We have to create new Directory as Temp and copy all files with extension .exe from Demo to temp.

import sys
import os
import shutil

def DirectoryCopyExt(SrcDir, DestDir, FileExt):
    Ret = False 
    Found = False

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

    for FolderName, SubFolderName, FileName in os.walk(SrcDir):
        for file in FileName:
            if file.endswith(FileExt):
                if not Found:
                    print(f"\nCopying '{FileExt}' files from '{SrcDir}' to '{DestDir}':\n")
                    Found = True

                src_path = os.path.join(FolderName, file)
                dest_path = os.path.join(DestDir, file)

                shutil.copy(src_path, dest_path)
                print(f"Copied: {src_path}")

    if not Found:
        print(f"There are no files with extension '{FileExt}' in '{SrcDir}'")

def main():
    Border = "-" * 51
    print(Border)
    print("--------- Marvellous Directory Automation ---------")
    print(Border)

    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        print("Usage : ScriptName DirectoryName1 DirectoryName2 FileExtension")
        return

    DirectoryCopyExt(sys.argv[1], sys.argv[2], sys.argv[3])

    print(Border)
    print("--------- Marvellous Directory Automation ---------")
    print(Border)

if __name__ == "__main__":
    main()