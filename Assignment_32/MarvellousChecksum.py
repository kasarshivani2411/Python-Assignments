# MarvellousChecksum.py
import os
import hashlib
import logging
import hashlib
import time

def CalculateChecksum(FileName):
    """Calculate MD5 checksum of a file."""
    try:
        with open(FileName, "rb") as fobj:
            hobj = hashlib.md5()
            buffer = fobj.read(1024)
            while buffer:
                hobj.update(buffer)
                buffer = fobj.read(1024)
        return hobj.hexdigest()
    except Exception as e:
        return f"Error: {e}"

def DirectoryChecksum(DirName):
    Border = "-"*51
    timestamp = time.ctime()
    
    # Create a timestamped log file
    LogFileName = "MarvellousChecksum_%s.log" % timestamp
    LogFileName = LogFileName.replace(" ", "_").replace(":", "_")
    
    with open(LogFileName, "w") as fobj:
        fobj.write(Border + "\n")
        fobj.write("Marvellous Directory Checksum Automation\n")
        fobj.write("Directory: " + DirName + "\n")
        fobj.write("Log created at: " + timestamp + "\n")
        fobj.write(Border + "\n")
        
        # Validate directory
        if not os.path.exists(DirName):
            fobj.write(f"Directory '{DirName}' does not exist\n")
            return
        if not os.path.isdir(DirName):
            fobj.write(f"'{DirName}' is not a directory\n")
            return
        
        FileCount = 0
        for FolderName, SubFolderName, FileName in os.walk(DirName):
            for file in FileName:
                FileCount += 1
                fullPath = os.path.join(FolderName, file)
                checksum = CalculateChecksum(fullPath)
                fobj.write(f"File: {fullPath}  |  Checksum: {checksum}\n")
        
        if FileCount == 0:
            fobj.write("No files found in the directory.\n")
        
        fobj.write(Border + "\n")
        fobj.write(f"Total files processed: {FileCount}\n")
        fobj.write(Border + "\n")

# # Setup logging
# logging.basicConfig(filename="MarvellousChecksum.log",
#                     level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# def ValidateDirectory(DirName):
#     """Validate that the directory exists and is indeed a directory."""
#     try:
#         if not os.path.exists(DirName):
#             logging.error(f"Directory '{DirName}' does not exist")
#             return False
#         if not os.path.isdir(DirName):
#             logging.error(f"'{DirName}' is not a directory")
#             return False
#         return True
#     except Exception as e:
#         logging.exception(f"Error validating directory '{DirName}': {e}")
#         return False

# def CalculateChecksum(FileName):
#     """Calculate MD5 checksum of a file."""
#     try:
#         with open(FileName, "rb") as fobj:
#             hobj = hashlib.md5()
#             buffer = fobj.read(1024)
#             while buffer:
#                 hobj.update(buffer)
#                 buffer = fobj.read(1024)
#         return hobj.hexdigest()
#     except Exception as e:
#         logging.exception(f"Error calculating checksum for file '{FileName}': {e}")
#         return None

# def CalculateDirectoryChecksums(DirectoryName):
#     """Traverse directory and calculate checksum for all files."""
#     if not ValidateDirectory(DirectoryName):
#         return

#     Found = False
#     try:
#         for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
#             for fName in FileName:
#                 fullPath = os.path.join(FolderName, fName)
#                 checksum = CalculateChecksum(fullPath)
#                 if checksum:
#                     if not Found:
#                         logging.info(f"Checksums of files in directory '{DirectoryName}':")
#                         Found = True
#                     logging.info(f"File: {fullPath}  |  Checksum: {checksum}")
#     except Exception as e:
#         logging.exception(f"Error traversing directory '{DirectoryName}': {e}")

#     if not Found:
#         logging.info(f"No files found in directory '{DirectoryName}'")