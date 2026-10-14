Div = lambda No : No%3==0 and No%5==0

def main():
    Data = [10,13,15,30,45,9,20]
    print("Input data is:",Data)

    FData = list(filter(Div,Data ))
    print("Data after filter:",FData)

if __name__ == "__main__":
    main()