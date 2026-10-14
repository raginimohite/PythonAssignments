def Binary(No):
    binary = ""
    
    while No > 0:
        rem = No%2
        binary = str(rem) + binary
        No = No//2

    return binary

def main():
    print("Enter a number")
    No = int(input())

    Result = Binary(No)
    print("Binary Equivalent:",Result)

if __name__ =="__main__":
    main()