Power = lambda No : No*No

def main():
    print("Enter your number:")
    value = int(input())
    result = Power(value)
    print("power of number is:",result)

if __name__ == "__main__":
    main()