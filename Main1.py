import MarvellousNum

def ListPrime(arr):
    sum = 0
    for i in arr:
        if MarvellousNum.ChkPrime(i):
            sum = sum + i

    return sum

def main():
    num =int(input("Enter number of elements:"))
    data = []
    print("enter elements:")
    for i in range(num):
        value = int(input())
        data.append(value)
    ans = ListPrime(data)

    print("Addition of prime numbers is:",ans)

if __name__=="__main__":
    main()

