import Arithmetic

def main():
    print("Enter first number")
    Value1 = int(input())
    
    print("Enter second number")
    Value2 = int(input())


    Ret = Arithmetic.Add(Value1 , Value2)  

    print("Addition is:",Ret)

    Ret = Arithmetic.Sub(Value1 , Value2)  

    print("Substaction is is:",Ret)

    Ret = Arithmetic.Mult(Value1 , Value2)  

    print("Multiplication is:",Ret)

    Ret = Arithmetic.Div(Value1 , Value2)  

    print("Division  is:",Ret)

if __name__ =="__main__":
    main()