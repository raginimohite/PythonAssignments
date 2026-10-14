import os
import time
import schedule
import datetime

def CountFiles(path):
    count = 0

    for item in os.listdir(path):
        fullpath = os.path.join(path,item)

        if os.path.isfile(fullpath):
            count = count + 1
        
        file = open("DirectoryCountLog.txt","a")
        file.write("Directory:" + path + "\n")
        file.write("Total Files:" + str(count)+"\n")
        file.write("Date and Time:" + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
        file.write("------------------------------------\n")
        file.close()
        print("Entry added to DirectoryCountLog.txt")

def main():

    path = input("Enter directory path:")
    if os.path.exists(path):
            
        schedule.every(5).minutes.do(CountFiles,path)

        print("Counting started:")

        while True:
            schedule.run_pending()
            time.sleep(1)
        else:
            print("Directory does not exist.")

if __name__ == "__main__":
    main()
        