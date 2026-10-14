def check(character):
    if character in "aeiouAEIOU":
        print("Vowel")
    else:
        print("Consonant")

def main():
    print("Enter a character")
    ch = input("character")
    check(ch)
    
    

if __name__ == "__main__":
    main()


