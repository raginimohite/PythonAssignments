def Max(arr):
    max = arr[0]
    for i in arr:
        if i > max:
         max = i
    return max

def main():
    num = int(input("Enter number of elements:"))
    data= []
    print("Enter elements:")
    for i in range(num):
        no = int(input())
        data.append(no)

    ans = Max(data)
    print("maximum number is :",ans)

if __name__ == "__main__":
    main()
