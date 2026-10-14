def Minimum(arr):
    min = arr[0]
    for i in arr:
        if i < min:
         min = i
    return min

def main():
    num = int(input("Enter number of elements:"))
    data= []
    print("Enter elements:")
    for i in range(num):
        no = int(input())
        data.append(no)

    ans = Minimum(data)
    print("minimum number is :",ans)

if __name__ == "__main__":
    main()
