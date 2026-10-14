def Tf(No):
    if No%5 == 0:
        print("true")

    else:
        print("false")

def main():
    print("Enter your number")
    num = int(input())
    Tf(num)

if __name__ == "__main__":
    main()