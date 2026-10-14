def calculate(No1,No2):
    print("Addition",No1 + No2)
    print("Substraction",No1 - No2)
    print("Multiplication",No1 * No2)
    print("Division",No1 / No2)

def main():
    print("Enter a number")
    num1 = int(input())
    print("Enter a second number")
    num2 = int(input())
    calculate(num1,num2)

if __name__ == "__main__":
    main()

