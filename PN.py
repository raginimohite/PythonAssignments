def Pn(No):
    if No > 0:
        print("positive number")

    elif No < 0:
        print("negative number")

    else:
        print("zero")

def main():
    print("Enter your number")
    num = int(input())
    Pn(num)

if __name__ == "__main__":
    main()