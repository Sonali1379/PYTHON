class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def info(self):
        return f"{self.name} (ID: {self.emp_id})"


class Developer(Employee):
    def role(self):
        return f"{self.info()} — Developer"


class Manager(Employee):
    def role(self):
        return f"{self.info()} — Manager"


if __name__ == "__main__":
    dev = Developer("Sam", 201)
    mgr = Manager("Riya", 301)
    print(dev.role())
    print(mgr.role())
