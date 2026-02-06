# DirectoryChecksum.py
import sys
import logging
# from MarvellousChecksum import CalculateDirectoryChecksums
from MarvellousChecksum import DirectoryChecksum

def main():
    Border = "-"*51
    print(Border)
    print("--------- Marvellous Directory Automation ---------")
    print(Border)
    
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        print("Usage: python DirectoryChecksum.py <DirectoryName>")
        return
    
    DirectoryChecksum(sys.argv[1])
    
    print(Border)
    print("--------- Marvellous Directory Automation ---------")
    print(Border)

if __name__ == "__main__":
    main()

# def main():
#     Border = "-"*51
#     logging.info(Border)
#     logging.info("--------- Marvellous Directory Checksum Automation ---------")
#     logging.info(Border)

#     try:
#         if len(sys.argv) == 2:
#             DirName = sys.argv[1]
#             logging.info(f"Calculating checksums for directory: {DirName}")
#             CalculateDirectoryChecksums(DirName)
#         else:
#             logging.error("Invalid number of arguments")
#             logging.info("Usage: DirectoryChecksum.py <DirectoryName>")

#     except Exception as e:
#         logging.exception(f"Unhandled exception: {e}")

#     logging.info(Border)
#     logging.info("--------- Marvellous Directory Checksum Automation ---------")
#     logging.info(Border)

# if __name__ == "__main__":
#     main()