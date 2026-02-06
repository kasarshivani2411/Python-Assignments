# Design automation script which accept directory name and write names of duplicate files from that directory into log file named as Log.txt
# Log.txt file should be created into current directory.
    # Usage : DirectoryDuplicate.py "Demo"
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

def FindDuplicate(DirectoryName):
    if not os.path.exists(DirectoryName):
        print(f"Directory '{DirectoryName}' does not exist")
        return {}
    if not os.path.isdir(DirectoryName):
        print(f"'{DirectoryName}' is not a directory")
        return {}

    Duplicate = {}
    for FolderName, SubFolderName, FileNames in os.walk(DirectoryName):
        for fName in FileNames:
            fullPath = os.path.join(FolderName, fName)
            checksum = CalculateChecksum(fullPath)
            if checksum:
                if checksum in Duplicate:
                    Duplicate[checksum].append(fullPath)
                else:
                    Duplicate[checksum] = [fullPath]
    return Duplicate

def WriteDuplicateLog(DuplicateDict):
    with open("Log.txt", "w") as fobj:
        Result = list(filter(lambda x: len(x) > 1, DuplicateDict.values()))
        if not Result:
            fobj.write("No duplicate files found.\n")
            print("No duplicate files found. See Log.txt for confirmation.")
        else:
            fobj.write("Duplicate files found:\n")
            for value in Result:
                for subValue in value:
                    fobj.write(subValue + "\n")
                fobj.write("\n")  # separate groups of duplicates
            print("Duplicate files written into Log.txt")

def main():
    Border = "-"*51
    print(Border)
    print("--------- Marvellous Directory Duplicate Finder ---------")
    print(Border)

    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        print("Usage: python DirectoryDuplicate.py <DirectoryName>")
        return

    DirName = sys.argv[1]
    DuplicateDict = FindDuplicate(DirName)
    WriteDuplicateLog(DuplicateDict)

    print(Border)
    print("--------- Marvellous Directory Duplicate Finder ---------")
    print(Border)

if __name__ == "__main__":
    main()