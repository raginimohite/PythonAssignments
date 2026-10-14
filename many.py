def mainy(No):
    for i in range(1,No+1):
        print(i)

def main():
    print("enter a number" )
    value=int(input())
    mainy(value)

if __name__=="__main__":
    main()