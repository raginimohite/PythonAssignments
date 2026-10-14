import psutil

def ProcessDisplay():
    fobj = open("ProcessLog.txt","w")
    for process in psutil.process_iter(['pid','name','username']):

        try:
            fobj.write(f"Name:{process.info['name']}\n")
            fobj.write(f"PID:{process.info['pid']}\n")
            fobj.write(f"Username:{process.info['username']}\n")
            fobj.write("-"*50+"\n")

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    fobj.close()

    print("log file created successfully")

def main():
    ProcessDisplay()

if __name__ == "__main__":
    main()
