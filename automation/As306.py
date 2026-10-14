import time
import schedule

def Lunch():
    print("Lunch time...")

def WrapUp():
    print("wrap up work...")

def main():
    schedule.every().day.at("13:00").do(Lunch)

    schedule.every().day.at("18:00").do(WrapUp)

    while True:
        print("schedule started...")

        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()
