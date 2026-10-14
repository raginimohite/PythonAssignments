def Grade(marks):

    if marks >= 75:
        print("Distinction")

    elif marks >=60:
        print("first class")

    elif marks >= 50:
        print("second class")

    else:
        print("fail")

def main():
    print("Enter marks")
    value = int(input())
    Grade(value)

if __name__ == "__main__":
    main()