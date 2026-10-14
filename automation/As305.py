import time
import schedule
import datetime

def WriteData():
    current = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    file = open("Marvellous.txt","a")
    file.write("Task executed at:"+ current + "\n")
    file.close()

    print("Data written successfully.")

def main():
    schedule.every(5).minutes.do(WriteData)
    print("scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()