class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student1 = Student("Sravi", 20, "Python")

print("Student Details:")
print(f"Name: {student1.name}")
print(f"Age: {student1.age}")
print(f"Course: {student1.course}")
