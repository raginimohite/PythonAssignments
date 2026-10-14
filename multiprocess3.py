from multiprocessing import Pool

def countprime(No):
    count = 0
    for i in range(2,No+1):
        prime = True
        for j in range(2,i):
            if i%j == 0:
                prime = False
                break
        if prime == True:
            count = count + 1
    
    print("Input number:",No)
    print("Prime:",count)
    return count
            
def main():
    numbers = [10000,20000,30000,40000]

    with Pool() as p:
        result = p.map(countprime,numbers)

    print("Input :",numbers)
    print("Output:",result)

    
if __name__ == "__main__":
    main()