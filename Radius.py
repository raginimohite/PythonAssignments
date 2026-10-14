def area(radius):
    return 3.14*radius *radius

def main():

    print("Enter radius")
    circle = float(input())

    result = area(circle)
    print("area of circle :",result)


if __name__ =="__main__":
        main()