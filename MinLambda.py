minimum = lambda no1,no2:  no1 if no1 < no2  else no2

def main():
  num1=int(input("Enter first number:"))
  num2=int(input("Enter second number:"))
  result=minimum(num1,num2)
  print("minimum number is:",result)

if __name__=="__main__":
    main()







