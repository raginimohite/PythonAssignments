def Add(arr):
    sum = 0
    for i in arr:
        sum = sum +i
    return sum

def main():
    num = int(input("Enter number of elements:"))
    data= []
    print("Enter elements:")
    for i in range(num):
        no = int(input())
        data.append(no)

    ans = Add(data)
    print("Addition is :",ans)

if __name__ == "__main__":
    main()
