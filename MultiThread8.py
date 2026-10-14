import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        lock.acquire()
        counter += 1
        lock.release()

def main():
    threads = []
    for i in range(5):
    
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("final counter value:",counter)

if __name__ == "__main__":
    main()



