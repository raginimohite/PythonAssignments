def factorSum(N):
    sum = 0
    for i in range(1,N):
        if N%i == 0:
         sum = sum + i
    return sum
        
def main():
    print("Enter your number")
    Value = int(input())

    result = factorSum(Value)
    print("sum of factors is:",result)

if __name__ == "__main__":
    main()
