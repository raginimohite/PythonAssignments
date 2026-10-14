import schedule
import time
import shutil
import os
import datetime

def Backup():
    source = input("Enter source path:")
    destination = input("Enter destination folder path:")

    current = datetime.datetime.now().strf("%d_%m_%Y_%H_%M_%s")
    filename = os.path.basename(source) 
    name,ext = os.path.splitext(filename)

    backup_file = destination + "\\" + name + "_" + current + ext
    shutil.copy(source,backup_file)
    logfile = open("backup_log.txt","a")
    logfile.write("Backup completed successfully at:"+ datetime.datetime.now().strf("%d_%m_%Y_ %I:%M:%S %p")+"\n")
    logfile.close()

    print("Backup completed Successfully")

def main():
    schedule.every(5).hours.do(Backup)
    print("scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()