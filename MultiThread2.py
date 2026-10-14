import threading
def SumEven(No):
    Sum=0
    for i in range(2,No+1,2):
        if No%i==0:
            Sum = Sum+i
            
    print("Summation of even factor:",Sum)

def SumOdd(No):
    Sum=0
    for i in range(1,No+1,2):
        if No%i==0:
            Sum = Sum+i
    print("Summation of odd factor:",Sum)

def main():

    t1 = threading.Thread(target=SumEven,args=(10,))
    t2 = threading.Thread(target=SumOdd,args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()