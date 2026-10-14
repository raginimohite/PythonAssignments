def Pattern(N):
    for i in range(N):
          for j in range(N):
               print("i",end=" ")
          print()
      
       
def main():
    print("Enter your number:")
    num = int(input())
    Pattern(num)

if __name__ == "__main__":
    main()