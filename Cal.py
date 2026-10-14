print("Which operation should you do from add, sub,mul,div : ")
operation=str(input())
print("enter first number")
No1=int(input())     
print("Enter second number")
No2=int(input())
if(operation=="add"):
    Ans=No1+No2
elif(operation=="sub"):
    Ans=No1-No2
elif(operation=="mul"):
    Ans=No1*No2
elif(operation=="div"):
    ANs=No1/No2
else:
    ("invalid")

print("result is:",Ans)


