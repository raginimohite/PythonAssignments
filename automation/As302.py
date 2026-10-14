import datetime
import time
import schedule

def Display():
    print("current date and time",datetime.datetime.now())

def main():
    print("Automation script started")

    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("end of automation script")


    

if __name__ == "__main__":
    main()