from multiprocessing import Pool
import os

def counteven(No):
    count = 0
    for i in range(2,No+1,2):
        count = count + 1

    print("Process ID:",os.getpid())
    print("Input number:",No)
    print("count of even numbers :",count)

    return count

def main():
    Data = [1000000,2000000,3000000,4000000]

    with Pool() as p:
        result = p.map(counteven,Data)
    
if __name__ == "__main__":
    main()





   