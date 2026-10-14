def Countdigit(No):
    count = 0
    while No > 0 :
        count = count+ 1
        No = No // 10
    return count
        
def main():
    print("Enter your number")
    value = int(input())

    Result = Countdigit(value)
    print("Count of Digits =",Result)

if __name__ == "__main__":
    main()



