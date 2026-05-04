school_name = "ABC Public School"  # Global variable


class Student:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        grade = "A"  # Local variable
        print(f"Student Name: {self.name}")
        print(f"School Name (Global): {school_name}")
        print(f"Grade (Local): {grade}")


student1 = Student("Sravi")
student1.show_details()
