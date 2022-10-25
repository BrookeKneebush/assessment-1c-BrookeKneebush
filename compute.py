class Shape:
    def __init__(self, number, shape_name, area):
        self.number = number
        self.shape_name = shape_name
        self.area = area

    def __str__(self):
        return f"{self.number} - {self.shape_name} with area size {self.area}\n"

square1 = Shape("1", "Square", 150.5)
rectangle1 = Shape("2", "Rectangle", 80)
rectangle2 = Shape("3", "Rectangle", 660)
circle1 = Shape("4", "Circle", 68.2)
triangle1 = Shape("5", "Triangle", 20)

print(square1, rectangle1, rectangle2, circle1, triangle1, sep="")
