from functools import reduce

Addition = lambda No1,No2:No1+No2


def main():
    Data = [13,12,8,10,11,20]

    print("Input data is :",Data)

    RData = reduce(Addition,Data)

    print("Data after reduce:",RData)

if __name__== "__main__":
    main()