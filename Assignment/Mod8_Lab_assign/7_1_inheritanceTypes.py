class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


# ----- 2. Multiple inheritance -----
# One child class inherits from more than one parent class.

class Flyer:
    def fly(self):
        return "Flying"


class Swimmer:
    def swim(self):
        return "Swimming"


class Duck(Flyer, Swimmer):
    def move(self):
        return f"{self.fly()} and {self.swim()}"


# ----- 3. Multilevel inheritance -----
# Chain: Grandparent -> Parent -> Child.

class LivingBeing:
    def alive(self):
        return True


class Mammal(LivingBeing):
    def warm_blooded(self):
        return True


class Human(Mammal):
    def think(self):
        return "Can think"


# ----- 4. Hierarchical inheritance -----
# Multiple child classes inherit from the same parent.

class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


# ----- 5. Hybrid inheritance -----
# Combination of multiple and multilevel (or hierarchical + multiple).

class A:
    def method_a(self):
        return "A"


class B(A):
    def method_b(self):
        return "B"


class C(A):
    def method_c(self):
        return "C"


class D(B, C):
    def method_d(self):
        return "D"


if __name__ == "__main__":
    print("=== Single inheritance ===")
    d = Dog()
    print(d.speak())

    print("\n=== Multiple inheritance ===")
    duck = Duck()
    print(duck.move())

    print("\n=== Multilevel inheritance ===")
    h = Human()
    print(f"Alive: {h.alive()}, Warm-blooded: {h.warm_blooded()}, {h.think()}")

    print("\n=== Hierarchical inheritance ===")
    r = Rectangle(4, 5)
    c = Circle(3)
    print(f"Rectangle area: {r.area()}, Circle area: {c.area()}")

    print("\n=== Hybrid inheritance ===")
    obj = D()
    print(obj.method_a(), obj.method_b(), obj.method_c(), obj.method_d())
