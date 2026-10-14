Checklength = lambda str : len(str) > 5

def main():
    Data = ["ragini" ,"khari" ,"sadi" ,"sanii","sakshi"]
    print("Input Data is:",Data)

    FData = list(filter(Checklength,Data))
    print("Data after filter:",FData)

if __name__ == "__main__":
    main()

