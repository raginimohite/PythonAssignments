def Area(length,width):
    return length*width

def main():
    print("enter a length")
    length=float(input())

    print("enter a width")
    width=float(input())

    result=Area(length,width)
    print("Area of rectangle:",result)

if __name__ == "__main__":
    main()




