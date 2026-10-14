import threading

def is_prime(No):
    if No <=1:
        return False
    for i in range(2,No):
        if No%i == 0:
            return False
    return True

def display_Prime(N):
    print("prime numbers:")
    for num in N:
        if is_prime(num):
            print(num,end=" ")
    print()

def display_NonPrime(N):
    print("non prime numbers:")
    for num in N:
        if not is_prime(num):
            print(num,end=" ")
    print()

def main():
    numbers = list(map(int,input("enter numbers separeted by space:").split()))
    t1 = threading.Thread(target=display_Prime,args=(numbers,))
    t2 = threading.Thread(target=display_NonPrime,args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()



