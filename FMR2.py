from functools import reduce

Even = lambda No: No%2==0
            
Square = lambda No: No * No

Addition = lambda No1,No2: No1+No2

def main():
    Data = [5,2,3,4,3,4,1,2,8,10]
    print("Input data is:",Data)

    FData = list(filter(Even,Data))
    print("Data after filter:",FData)

    MData = list(map(Square,FData))
    print("Data after map:",MData)

    RData = reduce(Addition,MData)
    print("Data after reduce:",RData)

if __name__ == "__main__":
    main()
    
