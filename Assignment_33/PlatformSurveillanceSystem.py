# Please follow below rules while designing automation script as :
# 1) Accept input through command line or through file
# 2) Display any message in log file instead of console
# 3) For separate task define separate function
# 4) For robustness handle every expected exception
# 5) Perform validations before taking any action
# 6) Create user defined mdules to store the functionality

# Add below features in Platform Surveillance System Project

# 1) Add Thread Monitoring Feature
    # For each running process, display:
        # a) Process Name
        # b) PID
        # c) Number of Threads created by that process
    # Requirement:
        # Store information in log file along with timestamp


# 2) Add Open Files Monitoring Feature
    # For each process, display:
        # Number of files opened by the process 
    # Requirement
        # a) Count open file descriptors using system/library calls
        # b) Handle permission errors properly
        # Mention "Access Denied" in log if required

# 3) Add Actual Memory Allocation Feature
    # Display real memory usage of each process:
        # a) RSS (Resident Set Size - actual RAM used)
        # b) VMS (Virtual Memory)
        # Memory Percentage
    # Requirement
        # Show:
            # Top 10 memory consuming processes

# 4) Add Periodic Email reporting Feature
    # Automatically send system report through email at regular intervals
    # Email must contain:
        # a) Log file attachment
        # b) Summary of:
            # 1. Total processes
            # 2. Top CPU usage processes
            # 3. Top memory usage processes
            # 4. Top Thread count processes
            # 5. Top Open file processes
    # Usage
        # PlatformSurveillanceSystem.py "MarvellousLogs" "receiver@gmail.com" 10
        # python PlatformSurveillanceSystem.py MarvellousLogs kasarshivani24@gmail.com 10
        # where:
            # 1. MarvellousLogs -> log folder
            # 2. receiver@gmail.com -> receiver mail
            # 3. 10 -> interval in minutes

# Expected Output in Log File
    # Each process entry should include:
            # 1. Process Name
            # 2. PID
            # 3. CPU %
            # 4. Memory (RSS)
            # 5. Threads Count
            # 6. Open Files Count
            # 7. Timestamp


import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage

def CreateLog(FolderName):
    Border = "-"*51
    
    Ret = False
    Ret = os.path.exists(FolderName)
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)
    print("Log file gets created with name :",FileName)

    fobj = open(FileName, "w")
    
    fobj.write(Border+"\n")
    fobj.write("----- Marvellous Platform Surveillance System -----\n")
    fobj.write("Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write(Border+"\n")
    fobj.write("------------------ System Report ------------------\n")
    fobj.write(Border+"\n")

    # print("CPU Usage :", psutil.cpu_percent())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    # print("RAM Usage :", mem.percent)
    fobj.write("RAM Usage : %s %%\n" %mem.percent)
    fobj.write(Border+"\n")

    fobj.write("\nDisk Usage Report\n")
    for part in psutil.disk_partitions():
        try :
            usage = psutil.disk_usage(part.mountpoint)
            # print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %% used\n" %(part.mountpoint, usage.percent))
        except:
            pass
    fobj.write(Border+"\n")

    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(net.bytes_sent/(1024 * 1024)))
    fobj.write("Recv : %.2f MB\n" %(net.bytes_recv/(1024 * 1024)))
    fobj.write(Border+"\n")

    # Process Log
    Data = ProcessScan()

    fobj.write("\nTop 10 Memory Consuming Processes\n")
    fobj.write(Border+"\n") 
    
    for info in Data:
        fobj.write("Process Name : %s\n" %info.get("name"))
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("CPU %% : %.2f\n" %info.get("cpu_percent"))
        if isinstance(info.get("rss"), int):
            fobj.write("Memory (RSS) : %.2f MB\n" % (info.get("rss") / (1024 * 1024)))
            # fobj.write("VMS : %.2f MB\n" % (info.get("vms") / (1024 * 1024)))
            # fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
        else:
            fobj.write("Memory (RSS) : Access Denied\n")
            # fobj.write("VMS : Access Denied\n")
            # fobj.write("Memory %% : Access Denied\n")
        fobj.write("Thread Count : %s\n" %info.get("num_threads"))
        fobj.write("Open File count : %s\n" %info.get("open_files"))
        fobj.write("Log created at : "+time.ctime()+"\n")
        # fobj.write("UserName : %s\n" %info.get("username"))
        # fobj.write("Status : %s\n" %info.get("status"))
        # fobj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
        
        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("----------------- End of Log File -----------------\n")
    fobj.write(Border+"\n")

    fobj.close()
    return FileName

def ProcessScan():
    listprocess = []

    # Warm up for CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name", "username", "status", "create_time", "num_threads", "open_files"])
            # Convert create_time
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent(None)
            
            # Actual Memory Allocation
            try:
                mem_info = proc.memory_info()
                info["rss"] = mem_info.rss          # Resident Set Size
                info["vms"] = mem_info.vms          # Virtual Memory Size
                info["memory_percent"] = proc.memory_percent()
            except psutil.AccessDenied:
                info["rss"] = "Access Denied"
                info["vms"] = "Access Denied"
                info["memory_percent"] = "Access Denied"

            try:
                info["num_threads"] = proc.num_threads()
            except psutil.AccessDenied:
                info["num_threads"] = "Access Denied"

            try:
                info["open_files"] = len(proc.open_files())
            except psutil.AccessDenied:
                info["open_files"] = "Access Denied"
            except (psutil.NoSuchProcess, psutil.ZombieProcess):
                info["open_files"] = "N/A"

            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Sorting processes by memory percentage in Descending order
    listprocess = sorted(
        listprocess,
        key=lambda x: x["memory_percent"]
        if isinstance(x["memory_percent"], float) else 0,
        reverse=True
    )

    # Returning only Top 10 memory consuming processes
    return listprocess[:10]

def SendEmail(sender, app_password, receiver, subject, body, attachment_path):

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    # Attach log file
    with open(attachment_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)

    msg.add_attachment(file_data,
                       maintype="application",
                       subtype="octet-stream",
                       filename=file_name)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit()

def GenerateSummary(process_data):
    total_processes = len(process_data)

    top_cpu = sorted(process_data,
                     key=lambda x: x["cpu_percent"] if isinstance(x["cpu_percent"], float) else 0,
                     reverse=True)[:5]

    top_memory = sorted(process_data,
                        key=lambda x: x["memory_percent"] if isinstance(x["memory_percent"], float) else 0,
                        reverse=True)[:5]

    top_threads = sorted(process_data,
                         key=lambda x: x["num_threads"] if isinstance(x["num_threads"], int) else 0,
                         reverse=True)[:5]

    top_open_files = sorted(process_data,
                            key=lambda x: x["open_files"] if isinstance(x["open_files"], int) else 0,
                            reverse=True)[:5]

    summary = f"""
    Total Processes Running : {total_processes}

    Top 5 CPU Consuming Processes:
    {[(p['name'], p['cpu_percent']) for p in top_cpu]}

    Top 5 Memory Consuming Processes:
    {[(p['name'], p['memory_percent']) for p in top_memory]}

    Top 5 Thread Count Processes:
    {[(p['name'], p['num_threads']) for p in top_threads]}

    Top 5 Open File Processes:
    {[(p['name'], p['open_files']) for p in top_open_files]}
    """

    return summary

def CreateLogAndSendMail(folder, receiver):

    sender_email = "kasarshivani2411@gmail.com"
    app_password = "eung dbxt cbtr fysn"

    process_data = ProcessScan()

    log_file = CreateLog(folder)

    summary = GenerateSummary(process_data)

    subject = "Marvellous Platform Surveillance System Report"

    SendEmail(sender_email, app_password, receiver, subject, summary, log_file)

    print("Email Sent Successfully with Log File")

def main():    
    Border = "-"*51
    print(Border)
    print("----- Marvellous Platform Surveillance System -----")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to : ")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with the log")
            print("4 : Store information about processess")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usage")
            print("7 : Store information about secondary storage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # python PlatformSurveillanceSystem.py MarvellousLogs kasarshivani24@gmail.com 10 
    elif(len(sys.argv) == 4):
        print("Inside Projects logic")
        print("Directory Name : ", sys.argv[1])
        print("Receiver's email : ", sys.argv[2])
        print("Time Interval : ", sys.argv[3])

        # Apply the schedular
        schedule.every(int(sys.argv[3])).minutes.do(CreateLogAndSendMail, sys.argv[1], sys.argv[2])

        print("Platform Surveillance System Started Successfully")
        print("Directory Created with Name :", sys.argv[1])
        print("Time interval in minutes :", sys.argv[3])
        print("Mail will be sent to :", sys.argv[2])
        print("Press Ctrl+C to stop the execution")
        # Wait till abort
        try:
            while(True):
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nPlatform Surveillance System Stopped Successfully")

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("--------- Thank you for using our script ----------")
    print(Border)

if __name__ == "__main__":
    main()