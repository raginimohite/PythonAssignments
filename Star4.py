def Pattern(N):
    for i in range(1,N+1):
          for j in range(1,i+1,):
               print(j,end=" ")
          print()
      
       
def main():
    print("Enter your number:")
    num = int(input())
    Pattern(num)

if __name__ == "__main__":
    main()