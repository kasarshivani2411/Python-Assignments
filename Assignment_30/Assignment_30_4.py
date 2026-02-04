# Copy File Contents into Another File
# Problem Statement : Write a program which accepts two file names from the user:
    # First file is an existing file
    # Second file is a new file
# Copy all contents from the first file into second file
# Input : ABC.txt Demo.txt
# Expected Output : Contents of ABC.txt copied into Demo.txt.

def CopyFileContents(fName1, fName2):
    src = open(fName1, "r")
    dest = open(fName2, "w")

    dest.write(src.read())

    print("Contents copied successfully into Demo.txt")

    src.close()
    dest.close()

def main():
    FileName1 = input("Enter the first file name : ")
    FileName2 = input("Enter the second file name : ")

    CopyFileContents(FileName1, FileName2)

if __name__ == "__main__":
    main()