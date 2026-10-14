import os
import schedule
import time
import datetime

def MonitorFile():
    filepath = "Demo.txt"
    logfile = "FileSizeLog.txt"
    file = open(logfile,"a")
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        file.write("file Path:" + os.path.abspath(filepath)+"\n")
        file.write("file size:"+str(size)+ "bytes\n")
        file.write("Date and time:"+ datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")+"\n")
        
        print("file sized logged successfully...")

    else:
        file.write("file does not eists:")
        file.write("Date and time:"+ datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")+"\n")
        file.write("---------------------------------------------------")
        print("file does not exists...")
        file.close()

def main():

    schedule.every(30).seconds.do(MonitorFile)
    print("scheduler started:")

    while True:
     schedule.run_pending()
     time.sleep(1)

if __name__ == "__main__":
   main()

    
