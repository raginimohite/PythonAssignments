print("Which operation should yuo do from Addition, sub, mul, div: ")
operation = str(input())

print("Enter first number : ")
No1 = int(input())

print("Enter Second number : ")
No2 = int(input())

if(operation=="Addition"):
    Ans=No1+No2
elif(operation=="sub"):
    Ans=No1-No2
elif(operation=="mul"):
     Ans=No1*No2
elif(operation=="div"):
     Ans=No1/No2
else:
     print("invalid")

    

print("Result is :",Ans)