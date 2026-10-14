import psutil
import os
import sys
import smtplib
from email.message import EmailMessage

def CreateLog(dirname):

    if not os.path.exists(dirname):
        os.mkdir(dirname)

    filename = os.path.join(dirname, "ProcessLog.txt")

    fobj = open(filename,"w")

    for process in psutil.process_iter(['pid','name','username']):
        try:
            fobj.write(f"Name : {process.info['name']}\n")
            fobj.write(f"PID : {process.info['pid']}\n")
            fobj.write(f"Username : {process.info['username']}\n")
            fobj.write("-"*50+"\n")

        except(psutil.NoSuchProcess,
               psutil.AccessDenied,
               psutil.ZombieProcess):
            pass

    fobj.close()

    return filename


def SendMail(emailid,filename):

    msg = EmailMessage()

    msg["Subject"] = "Process Log File"
    msg["From"] = "youremail@gmail.com"
    msg["To"] = emailid

    msg.set_content("Attached is the Process Log File.")

    with open(filename,"rb") as f:
        filedata = f.read()

    msg.add_attachment(filedata,
                       maintype="text",
                       subtype="plain",
                       filename="ProcessLog.txt")

    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login("youremail@gmail.com","Your_App_Password")

    server.send_message(msg)

    server.quit()

    print("Mail sent successfully")


def main():

    if len(sys.argv)!=3:
        print("Usage : python AS342.py Directory Email")
        return

    filename = CreateLog(sys.argv[1])

    SendMail(sys.argv[2],filename)

if __name__ == "__main__":
    main()

