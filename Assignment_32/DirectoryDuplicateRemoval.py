# Design Automation script which accept directory name and delete all duplicate files from that directory. Write names of duplicate files
# from that directory into log file named as Log.txt.
# Log.txt should be created into current directory
    # Usage : DirectoryDuplicateRemoval.py "Demo"
# Demo is name of directory

import hashlib
import os
import sys

def CalculateChecksum(FileName):
    try:
        with open(FileName, "rb") as fobj:
            hobj = hashlib.md5()
            buffer = fobj.read(1024)
            while buffer:
                hobj.update(buffer)
                buffer = fobj.read(1024)
        return hobj.hexdigest()
    except Exception as e:
        return None

def FindDuplicates(DirectoryName):
    if not os.path.exists(DirectoryName):
        print(f"Directory '{DirectoryName}' does not exist")
        return {}
    if not os.path.isdir(DirectoryName):
        print(f"'{DirectoryName}' is not a directory")
        return {}

    DuplicateDict = {}
    for FolderName, SubFolders, FileNames in os.walk(DirectoryName):
        for fName in FileNames:
            fullPath = os.path.join(FolderName, fName)
            checksum = CalculateChecksum(fullPath)
            if checksum:
                if checksum in DuplicateDict:
                    DuplicateDict[checksum].append(fullPath)
                else:
                    DuplicateDict[checksum] = [fullPath]
    return DuplicateDict

def DeleteDuplicates(DuplicateDict):
    with open("Log.txt", "w") as fobj:
        Result = list(filter(lambda x: len(x) > 1, DuplicateDict.values()))
        if not Result:
            fobj.write("No duplicate files found.\n")
            print("No duplicate files found. See Log.txt for confirmation.")
            return

        fobj.write("Deleted duplicate files:\n")
        TotalDeleted = 0

        for files in Result:
            # Keep first file, delete the rest
            for file in files[1:]:
                try:
                    os.remove(file)
                    fobj.write(file + "\n")
                    TotalDeleted += 1
                except Exception as e:
                    fobj.write(f"Failed to delete {file}: {e}\n")

        fobj.write(f"\nTotal duplicate files deleted: {TotalDeleted}\n")
        print(f"Total duplicate files deleted: {TotalDeleted}. See Log.txt for details.")

def main():
    Border = "-"*51
    print(Border)
    print("--------- Marvellous Directory Duplicate Removal ---------")
    print(Border)

    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        print("Usage: python DirectoryDuplicateRemoval.py <DirectoryName>")
        return

    DirName = sys.argv[1]
    DuplicateDict = FindDuplicates(DirName)
    DeleteDuplicates(DuplicateDict)

    print(Border)
    print("--------- Marvellous Directory Duplicate Removal ---------")
    print(Border)

if __name__ == "__main__":
    main()