larger = lambda no1,no2,no3:  no1 if no1 > no2 and no1>no3 else no2 if no2>no3 else no3

def main():
  num1=int(input("Enter first number:"))
  num2=int(input("Enter second number:"))
  num3=int(input("Enter second number:"))
  result=larger(num1,num2,num3)
  print("larger number is:",result)

if __name__=="__main__":
    main()







