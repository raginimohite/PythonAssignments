def factor(No):
    for i in range(1,No+1):
        if No % i == 0:
            print(i)

def main():
    print("Enter a number")
    value= int(input())
    factor(value)
if __name__== "__main__":
    main()
    