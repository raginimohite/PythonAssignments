def perfect(No):
    sum = 0
    for i in range(1,No):
        if No % i == 0:
            sum = sum + i
    if sum==No:
         return True
    else:
         return False

        
def main():
    print("Enter a number")
    No = int(input())
    if perfect(No):
            print("number is perfect")
    else:
            print("number is not perfect")
    

if __name__ == "__main__":
    main()