def PalindromeNo(No):
    original = No
    rev = 0
    while No > 0:
        digit = No % 10
        rev = rev * 10 + digit
        No = No //10
    
    if original == rev:
        print("palindrome number")
    else:
        print("not pailindrome number")
    
def main():
    print("enter your number")
    value = int(input())
    PalindromeNo(value)

if __name__ == "__main__":
    main()