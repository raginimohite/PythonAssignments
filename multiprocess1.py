from multiprocessing import Pool

def sumsquares(n):
    total = 0
    for i in range(1,n+1):
        total = total +(i*i)
    return total

def main():
    numbers = [1000000,2000000,3000000,4000000]

    with Pool() as p:
        result = p.map(sumsquares,numbers)

    print("Input:",numbers)
    print("output:",result)

if __name__ == "__main__":
    main()