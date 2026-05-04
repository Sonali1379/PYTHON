class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def describe(self):
        base = super().area()
        return f"Square with side {self.width}, area from parent logic: {base}"


if __name__ == "__main__":
    sq = Square(5)
    print(sq.describe())
    print("area() via super chain:", sq.area())
