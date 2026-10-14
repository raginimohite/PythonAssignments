maximum = lambda no1,no2:  no1 if no1 > no2  else no2

def main():
  num1=int(input("Enter first number:"))
  num2=int(input("Enter second number:"))
  result=maximum(num1,num2)
  print("maximum number is:",result)

if __name__=="__main__":
    main()







