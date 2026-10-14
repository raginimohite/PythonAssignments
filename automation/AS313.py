import os
import time
import schedule
import datetime

def ScanDirectory(path):
    files = 0
    folders = 0

    for item in os.listdir(path):
        fullpath = os.path.join(path,item)

        if os.path.isfile(fullpath):
            files = files + 1
        elif os.path.isdir(fullpath):
            folders = folders + 1

    print("\nDirecctory  Scanned:",path)
    print("Total files  :",files)
    print("Total subdirectories:",folders)
    print("Scan time :",datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    path = input("Enter directory path:")
    print(path)
    if os.path.exists(path):
        schedule.every(1).minutes.do(ScanDirectory,path)

        print("Directory scanning started:")

        while True:
            schedule.run_pending()
            time.sleep(1)
        else:
            print("Directory does not exist.")

if __name__ == "__main__":
    main()