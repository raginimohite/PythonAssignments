import schedule
import time

def DisplayMessage(message):
    print(message)

def main():

    message = input("Enter a message:")
    interval = int(input("enter interval in seconds:"))

    if interval <= 0:
        print("interval must be greater than zero:")

    else:
        schedule.every(interval).seconds.do(DisplayMessage,message)

        print(f"\nDisplaying '{message}' every {interval} seconds...\n")

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__== "__main__":
    main()