from functools import reduce
def Prime(No1):
    if No1 < 2:
        return False
    for i in range(2,No1):
       if No1%i==0:
        return False
    return True
def Multi(No1):
    return No1 * 2
def Max(No1,No2):
      return No1 if No1 > No2 else No2
def main():
    Data = [2,70,11,10,17,23,31,77]

    print("Input data is :",Data)

    FData = list(filter(Prime,Data))

    print("Data after filter:",FData)

    MData = list(map(Multi,FData))

    print("Data after map:",MData)

    RData = reduce(Max,MData)

    print("Data after reduce:",RData)

if __name__== "__main__":
    main()