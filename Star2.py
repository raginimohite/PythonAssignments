def Pattern(N):
    for i in range(N,0,-1):
          for j in range(i):
               print("*",end=" ")
          print()
      
       
def main():
    print("Enter your number:")
    num = int(input())
    Pattern(num)

if __name__ == "__main__":
    main()