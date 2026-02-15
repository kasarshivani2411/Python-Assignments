# Please follow below rules while designing automation script as :
# 1) Accept input through command line or through file
# 2) Display any message in log file instead of console
# 3) For separate task define separate function
# 4) For robustness handle every expected exception
# 5) Perform validations before taking any action
# 6) Create user defined modules to store the functionality

# Add below features in Marvellous Data Shield System Project

# 1) Logging System
    # Create a Logs/folder
    # Store:
        # 1. Backup start time
        # 2. Files copied
        # 3. Zip file name
        # 4. Errors (if any)

# 2) Email Notification
    # Send an email after backup completion
    # Attach:
        # 1. Log file
        # 2. Zip file name

# 3) Restore Feature
    # Add a command:
        # python MarvellousDataShieldSystem.py --restore ZipFileName Destination
    # Extract backup to given directory

# 4) Exclude Files/Folders
    # Ignore:
        # .tmp, .log, .exe
        # or user defined extensions

# 5) Backup History Tracker
    # Maintain a file:
        # 1. Date
        # 2. Number of files
        # 3. Zip size
    # Display history using:
        # python MarvellousDataShieldSystem.py --history

import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    # open the zip file
    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, folder)

            zobj.write(full_path, relative_path)

    zobj.close()

    return zip_name

def Calculate_hash(path):
    hobj = hashlib.md5()

    fobj = open(path, "rb")

    while(True):
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()

def BackupFiles(Source, Destination, exclude_ext = None):
    if exclude_ext is None:
        exclude_ext = [".tmp", ".log", ".exe"]

    copied_files = []

    print("Creating the backup folder for backup process")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:
            if any(file.endswith(ext) for ext in exclude_ext):
                continue

            src_path = os.path.join(root, file)
            relative_path = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative_path)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            try:
                # Copy the files if its new
                if((not os.path.exists(dest_path)) or (Calculate_hash(src_path) != Calculate_hash(dest_path))):
                    shutil.copy2(src_path, dest_path)
                    copied_files.append(relative_path)

            except Exception:
                print("Error copying:", file, str(Exception))

    return copied_files

def CreateBackupLog(files_copied, zip_name, errors):
    os.makedirs("Logs", exist_ok=True)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    logfile = os.path.join("Logs", f"BackupLog_{timestamp}.log")

    fobj = open(logfile, "w")

    fobj.write("-"*60 + "\n")
    fobj.write("Marvellous Data Shield Backup Log\n")
    fobj.write("Backup Start Time : " + time.ctime() + "\n")
    fobj.write("-"*60 + "\n\n")

    fobj.write(f"Total Files Copied : {len(files_copied)}\n\n")

    fobj.write("Files Copied:\n")
    for file in files_copied:
        fobj.write(file + "\n")

    fobj.write("\nZip File Created : " + zip_name + "\n")

    if errors:
        fobj.write("\nErrors:\n")
        for err in errors:
            fobj.write(err + "\n")

    fobj.write("\nBackup Completed At : " + time.ctime() + "\n")
    fobj.write("-"*60 + "\n")

    return logfile

def UpdateHistory(zip_name, file_count):
    history_file = "backup_history.txt"
    zip_size = os.path.getsize(zip_name) / (1024 * 1024)

    fobj = open(history_file, "a")
    fobj.write(f"{time.ctime()} | Files: {file_count} | Size: {zip_size:.2f} MB\n")


def ShowHistory():
    if not os.path.exists("backup_history.txt"):
        print("No backup history found.")
        return

    fobj = open("backup_history.txt", "r")
    print(fobj.read())

def SendBackupMail(sender, password, receiver, logfile, zipfile_name):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "Marvellous Backup Completed"

    body = f"""
Backup Completed Successfully.

Zip File Created : {zipfile_name}
Log File Attached.

Regards,
Marvellous
"""

    msg.set_content(body)

    with open(logfile, "rb") as f:
        msg.add_attachment(f.read(),
                           maintype="application",
                           subtype="octet-stream",
                           filename=os.path.basename(logfile))

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, password)
    smtp.send_message(msg)
    smtp.quit()

def RestoreBackup(zip_name, destination):
    if not os.path.exists(zip_name):
        print("Zip file not found")
        return

    os.makedirs(destination, exist_ok=True)

    zobj = zipfile.ZipFile(zip_name, 'r')
    zobj.extractall(destination)

    print("Backup Restored Successfully to", destination)


def MarvellousDataShieldStart(Source="Data"):
    Border = "-"*51
    errors = []

    try:
        BackupName = "MarvellousBackup"

        print(Border)
        print("Backup Process Started Successfully at :", time.ctime())
        print(Border)

        files = BackupFiles(Source, BackupName)
        
        zip_file = make_zip(BackupName)

        logfile = CreateBackupLog(files, zip_file, errors)

        UpdateHistory(zip_file, len(files))

        # === Email Config ===
        sender_email = "kasarshivani2411@gmail.com"
        app_password = "eung dbxt cbtr fysn"
        receiver_email = "kasarshivani24@gmail.com"

        SendBackupMail(sender_email, app_password, receiver_email, logfile, zip_file)

        print(Border)
        print("Backup completed successfully")
        print("Files copied :", len(files))
        print("Zip files gets created :", zip_file)
        print("Log File:", logfile)
        print(Border)

    except Exception:
        errors.append(str(Exception))
        CreateBackupLog([], "Not Created", errors)

def main():    
    Border = "-"*51
    print(Border)
    print("---------- Marvellous Data Shield System ----------")
    print(Border)

    # -------------------------------------------------
    # Restore Command
    # python MarvellousDataShieldSystem.py --restore ZipFile Destination
    # -------------------------------------------------
    if len(sys.argv) == 4 and sys.argv[1] == "--restore":
        RestoreBackup(sys.argv[2], sys.argv[3])
        print(Border)
        print("--------- Thank you for using our script ----------")
        print(Border)
        return

    # -------------------------------------------------
    # History Command
    # python MarvellousDataShieldSystem.py --history
    # -------------------------------------------------
    if len(sys.argv) == 2 and sys.argv[1] == "--history":
        ShowHistory()
        print(Border)
        print("--------- Thank you for using our script ----------")
        print(Border)
        return

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to : ")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archieve of the backup periodically")
            print("4 : Email will sent to the receiver of the backup zip file")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to back up")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # python Demo.py 5 Data 
    elif(len(sys.argv) == 3):
        print("Inside Projects logic")
        print("Time Interval : ", sys.argv[1])
        print("Directory Name : ", sys.argv[2])

        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])

        print(Border)
        print("Data Shield System Started Successfully")
        print("Time interval in minutes :", sys.argv[1])
        print("Press Ctrl+C to stop the execution")
        print(Border)

        try:
            # Wait till abort
            while(True):
                schedule.run_pending()
                time.sleep(1)

        except KeyboardInterrupt:
            print("\nSystem Stopped Successfully")

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("--------- Thank you for using our script ----------")
    print(Border)

if __name__ == "__main__":
    main()