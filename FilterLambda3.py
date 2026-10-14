CountDigits = lambda No:len([X for X in str(No) if int(X) % 2 ==0])
    


def main():
    Data = (2,3,4,5,6,7,8)
    print("Input Data is :",Data)

    FData = list(filter(CountDigits,Data))
    print("Data after filte:",FData)

    
if __name__ =="__main__":
    main()



