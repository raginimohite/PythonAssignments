from functools import reduce

def GreatLess (No):
    return No >= 70 and No <=90
            
def increase(No):
    return No + 10

def Product(No1,No2):
    return No1*No2

def main():
    Data = [4,34,36,76,68,24,89,23,86,90,45,70]
    print("Input data is:",Data)

    FData = list(filter(GreatLess,Data))
    print("Data after filter:",FData)

    MData = list(map(increase,FData))
    print("Data after map:",MData)

    RData = reduce(Product,MData)
    print("Data after reduce:",RData)

if __name__ == "__main__":
    main()
    
