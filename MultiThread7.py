import threading

def find_max(numbers):
    print("Maximum element:",max(numbers))

def find_min(numbers):
    print("minimum elements:",min(numbers))

def main():
    numbers = list(map(int,input("Enter numbers separeted by space:").split()))

    t1=threading.Thread(target=find_max,args=(numbers,))
    t2=threading.Thread(target=find_min,args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

    

