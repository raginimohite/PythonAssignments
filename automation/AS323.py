import os
import schedule
import time

def Readfile():
    filename = "Demo.txt"
    try:
        if not os.path.exists(filename):
            print("filename does not exists")
            return
        file = open(filename,"r")
        data = file.read()
        if len(data)==0:
            print("file is empty.")
        else:
            print("file contents.")
            print(data)
        file.close()

    except PermissionError:
        print("Permission is denied:")

    except OSError:
        print("file cannot be opened:")

def main():

    schedule.every(1).minutes.do(Readfile)
    print("scheduler started:")

    while True:
     schedule.run_pending()
     time.sleep(1)

if __name__ == "__main__":
   main()

    

