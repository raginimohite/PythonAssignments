import os
import time
import schedule
import datetime

def TimeStamp():

    filename = ("File_"+ datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")+".txt")
    with open(filename ,"w") as file:
        file.write("Filename:"+ filename + "\n")
        file.write("creation date:" + datetime.datetime.now().strftime("%d-%m-%Y") + "\n")
        file.write("creation Time:" + datetime.datetime.now().strftime("%H-%M-%S %p"))
        print(filename,"created succesfully:")
        file.close()

def main():

    schedule.every(1).minutes.do(TimeStamp)
    print("scheduler started:")

    while True:
     schedule.run_pending()
     time.sleep(1)

if __name__ == "__main__":
   main()

    
