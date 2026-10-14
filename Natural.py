def Natural(N):
    sum = 0
    for i in range(1,N+1):
        sum = sum + i
        print(sum)

def main():
    print("Enter your number")
    Value = int(input())
    Natural(Value)

if __name__ == "__main__":
    main()
