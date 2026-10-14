from multiprocessing import Pool
import os

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i

    print("Process ID:",os.getpid())
    print("Input number:",n)
    print("Factorial:",fact)

    return fact

def main():
    Data = [10,15,20,25]

    with Pool() as p:
        Result = p.map(factorial,Data)

    print("Final result:",Result)

if __name__ == "__main__":
    main()

