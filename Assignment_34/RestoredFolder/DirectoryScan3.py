import os

def DirectoryScanner(DirectoryName = "Marvellous"):
    Ret = os.path.exists(DirectoryName)
    
    if(Ret == False):
         print("There is no such directory")
         return
    
    print("Contents of the directory are :")
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder name :", FolderName)

        for subF in SubFolderName:
            print("SubFolder name :", subF)

        for fName in FileName:
                print("File name :", fName)
     

def main():
    DirectoryName = input("Enter the name of directory : ")

    DirectoryScanner(DirectoryName)

if __name__ == "__main__":
    main()