from multiprocessing import Pool
import time

def sumpower(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum +(i**5)

    return sum

def main():
    Data = [1000000,2000000,3000000,4000000]
    Start = time.perf_counter()
    with Pool() as p:
        result = p.map(sumpower,Data)
    End = time.perf_counter()

    print("Input:",Data)
    print("Output:",result)
    print("Execution Time:",End - Start,"seconds")

if __name__ == "__main__":
    main()