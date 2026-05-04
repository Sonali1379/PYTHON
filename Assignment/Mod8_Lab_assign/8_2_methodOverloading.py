class Calculator:
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        return a + b + c

    def total(self, *values):
        return sum(values)


if __name__ == "__main__":
    calc = Calculator()
    print("add(10, 20):", calc.add(10, 20))
    print("add(10, 20, 30):", calc.add(10, 20, 30))
    print("total(1, 2, 3, 4, 5):", calc.total(1, 2, 3, 4, 5))
