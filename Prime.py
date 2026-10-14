def prime(No):
    if No > 1 :
        for i in range(2,No):
            if (No % i == 0):
                print("number is not prime")
            
                return        
        print("number is prime")
        
                

def main():
    print("Enter your number")
    value = int(input())
    prime(value)

if __name__ == "__main__":
    main()



