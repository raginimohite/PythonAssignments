import os
import shutil
import schedule
import time
from datetime import datetime

def CopyTextFiles():

    source = input("Enter Source Directory : ")
    destination = input("Enter Destination Directory : ")

    if not os.path.exists(source):
        print("Source directory does not exist.")
        return

    if not os.path.exists(destination):
        print("Destination directory does not exist.")
        return

    logfile = open("CopyLog.txt", "a")

    for file in os.listdir(source):

        if file.endswith(".txt"):

            src = os.path.join(source, file)
            dest = os.path.join(destination, file)

            try:
                shutil.copy(src, dest)

                logfile.write("Copied : " + file + "\n")
                logfile.write("Time : " + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")
                logfile.write("---------------------------------\n")

                print(file, "Copied Successfully.")

            except Exception as e:
                print("Cannot copy :", file)
                logfile.write("Failed : " + file + "\n")
                logfile.write(str(e) + "\n")
                logfile.write("---------------------------------\n")

    logfile.close()

def StartScheduler():

    CopyTextFiles()

    schedule.every(10).minutes.do(CopyTextFiles)

    print("File Copy Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

def main():

    StartScheduler()

if __name__ == "__main__":
    main()