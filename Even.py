def Eve(N):
    for i in range(1,N+1):
        if i % 2 == 0:
            print(i)
        

def main():
    print("Enter your number")
    Value = int(input())
    Eve(Value)

if __name__ == "__main__":
    main()
