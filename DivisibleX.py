def Div(No):
    if(No%3==0 and No%5==0):
        print("Its Divisible by 3 and 5")
    else:
        print("Its not Divisible by 3 and 5")
    

def main():
            Value = int(input("Enter number:"))
            
            Div(Value)

if __name__ == "__main__":
    main()