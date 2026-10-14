import threading
def Small(S):
    count = 0
    for ch in S:
        if ch.islower():
            count = count + 1

    print("small letters count:",count) 
    print("Thread ID:",threading.get_ident())
    print("Thread name:",threading.current_thread().name)

def capital(S):
    count = 0
    for ch in S:
        if ch.isupper():
            count = count + 1

    print("Capital  letters count:",count) 
    print("Thread ID:",threading.get_ident())
    print("Thread name:",threading.current_thread().name)

def digits(S):
    count = 0
    for ch in S:
        if ch.isdigit():
            count = count + 1

    print("digits count:",count) 
    print("Thread ID:",threading.get_ident())
    print("Thread name:",threading.current_thread().name)



def main():
    S = input("Enter a string:")

    t1 = threading.Thread(target=Small,args=(S,),name = "smallthread")
    t2 = threading.Thread(target=capital,args=(S,),name = "capitalthread")
    t3 = threading.Thread(target=digits,args=(S,),name= "digitsthread")


    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()