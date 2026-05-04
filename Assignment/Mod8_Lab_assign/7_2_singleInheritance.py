class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}."


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def details(self):
        return f"{self.introduce()} Roll number: {self.roll_no}."


if __name__ == "__main__":
    s = Student("Alex", 101)
    print(s.introduce())
    print(s.details())
