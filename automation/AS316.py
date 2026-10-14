import time
import schedule

def goals():
    print("start your weekly goals...")

def Progress():
    print("Review your weekly progress...")

def Complete():
    print("Weekly work completed...")

def main():
    schedule.every().monday.at("09:00").do(goals)

    schedule.every().wednesday.at("17:00").do(Progress)

    schedule.every().friday.at("18:00").do(Complete)

    while True:
        print("schedule started...")

        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()
