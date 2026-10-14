def ChkNum(No):
    if No%2==0:
        print("Even number")
    else:
        print("Odd number")

def main():
    print("Enter your number")
    value = int(input())
    ChkNum(value)

if __name__ == "__main__":
    main()