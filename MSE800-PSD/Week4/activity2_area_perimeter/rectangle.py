class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def display(self):
        print("--------------------Result--------------------")
        print(f"Rectangle: width={self.width}, height={self.height}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")