def Div(No,No1):
    if(No%No1==0):
        print("Its Divisible by ",No1)
    else:
        print("not divisible by ",No1)
    

def main():
            Value1 = int(input("Enter number:"))
            Value2 = int(input("Enter divider:"))



            Div(Value1,Value2)

if __name__ == "__main__":
    main()