def factorial(N):
    fact = 1
    for i in range(1,N+1):
        fact = fact * i
        print(fact)

def main():
    print("Enter your number")
    Value = int(input())
    factorial(Value)

if __name__ == "__main__":
    main()
