from multiprocessing import Pool
import os

def sumeven(No):
    sum = 0
    for i in range(2,No+1,2):
        sum = sum + i

    print("Process ID:",os.getpid())
    print("Input number:",No)
    print("sum of even numbers :",sum)

    return sum

def main():
    Data = [1000000,2000000,3000000,4000000]

    with Pool() as p:
        result = p.map(sumeven,Data)
    print("final result:",result)

if __name__ == "__main__":
    main()





   