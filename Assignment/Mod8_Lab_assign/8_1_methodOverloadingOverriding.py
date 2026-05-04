class Calculator:
    def add(self, a, b, c=None):
        """Add two or three numbers depending on whether c is given."""
        if c is None:
            return a + b
        return a + b + c

    def total(self, *values):
        """Add any number of numeric arguments."""
        return sum(values)


class Shape:
    def area(self):
        return 0

    def describe(self):
        return "Generic shape"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

    def describe(self):
        return f"Circle, r={self.radius}, area={self.area()}"


if __name__ == "__main__":
    print("=== Method overloading (Python idioms) ===")
    calc = Calculator()
    print("add(2, 3):", calc.add(2, 3))
    print("add(2, 3, 4):", calc.add(2, 3, 4))
    print("total(1, 2, 3, 4):", calc.total(1, 2, 3, 4))

    print("\n=== Method overriding ===")
    s = Shape()
    c = Circle(3)
    print("Shape.area():", s.area(), "|", s.describe())
    print("Circle.area():", c.area(), "|", c.describe())
