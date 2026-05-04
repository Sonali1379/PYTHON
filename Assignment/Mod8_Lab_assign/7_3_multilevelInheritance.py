class Animal:
    def eat(self):
        return "Animal eats food."


class Mammal(Animal):
    def walk(self):
        return "Mammal walks on land."


class Dog(Mammal):
    def bark(self):
        return "Dog barks."


if __name__ == "__main__":
    d = Dog()
    print(d.eat())    # Inherited from Animal
    print(d.walk())   # Inherited from Mammal
    print(d.bark())   # Dog's own method
