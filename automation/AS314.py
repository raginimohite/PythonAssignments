import schedule
import time
import datetime

def CreateLogFile():
    filename = "MarvellousLog_" + datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    file = open(filename, "w")
    file.write("log file created successfully.\n")
    file.write("creation Time:" + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    file.close()

    print(filename,"created successfully.")

def main():
    schedule.every(5).minutes.do(CreateLogFile)
    print("Log file scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()