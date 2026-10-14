import threading
def SumEven(No):
    even = []
    Sum=0

    for i in No:
        if i%2==0:
            even.append(i)
            Sum = Sum + i

    print("even elements:",even) 
    print("Summation of even numbers:",Sum)

def SumOdd(No):
    odd = []
    Sum=0

    for i in  No:
        if i%2 !=0:
            odd.append(i)
            Sum = Sum + i

    print("odd elements:",odd) 
    print("Summation of odd numbers:",Sum)

def main():
    No= list(map(int,input("enter a numbers by space:").split()))

    t1 = threading.Thread(target=SumEven,args=(No,))
    t2 = threading.Thread(target=SumOdd,args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()