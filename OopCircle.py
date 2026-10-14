class circle():
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        self.radius = float(input("Enter radius:"))

    def CalculateArea(self):
        self.area = circle.PI*self.radius*self.radius

    def CalculateCircumference(self):
        self.circumference = 2 *circle.PI*self.radius

    def Display(self):
        print("Radius=",self.radius)
        print("Area=",self.area)
        print("Circumference=",self.circumference)


obj1 = circle()
obj2 = circle()

obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()


