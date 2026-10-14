from functools import reduce

product = lambda No1,No2:No1*No2

def main():
    Data = [4,6,9,5,2,3]
    print("Input data is:",Data)

    RData = reduce(product,Data)
    print("Data after reduce:",RData)

if __name__ == "__main__":
    main()
