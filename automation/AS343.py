import psutil
import sys
import os

def ProcessDisplay(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    filename = os.path.join(dirname,"ProcessLog.txt")

    fobj = open(filename ,"w")

    for process in psutil.process_iter(['pid','name','username']):

        try:
            
                fobj.write("process found\n")
                fobj.write(f"Name:{process.info['name']}\n")
                fobj.write(f"PID:{process.info['pid']}\n")
                fobj.write(f"Username:{process.info['username']}\n")
                fobj.write("-"*50+"\n")

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    
    fobj.close()

    print("log file created successfully")

def main():

    if len(sys.argv) != 2:
        print("Usage : python ProcInfo.py ProcessName")
        return
    ProcessDisplay(sys.argv[1])

if __name__ == "__main__":
    main()
