def reverseNo(No):
    rev = 0
    while No > 0:
        digit = No % 10
        rev = rev * 10 + digit
        No = No //10
    return rev
    
def main():
    print("enter your number")
    value = int(input())
    Result = reverseNo(value)
    print("riverse no is:",Result)

if __name__ == "__main__":
    main()