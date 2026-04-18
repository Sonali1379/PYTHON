class student:
    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email
    def display(self):
        print(self.id, self.name, self.email)

s1 = student(1,"sonali","sonali@example.com")
s1.display()


s2 = student(2,"sneha","sneha@example.com")
s2.display()