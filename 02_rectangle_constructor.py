class Rectangle:
    def __init__(self, height, breadth):
        self.height = height
        self.breadth = breadth

    def area(self):
        return self.height * self.breadth

shape = Rectangle(12, 6)
print("Area:", shape.area())
