def Even(No):
    print("even numbers are:")
    for i in range(2,No,2):
        print(i,end=" ")

def Odd(No):
    print("odd numbers are:")
    for i in range(1,No,2):
        print(i,end= " ")
    
def main():
    Even(20)
    Odd(20)
    

if __name__ == "__main__":
    main()