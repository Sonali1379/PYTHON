class Vehicle:
    def describe(self):
        return "A vehicle"


class Car(Vehicle):
    def wheels(self):
        return 4


class Bike(Vehicle):
    def wheels(self):
        return 2


class GarageSale(Car, Bike):
    """Inherits from two siblings that share the same parent (diamond / hybrid)."""

    def listing(self):
        return (
            f"{self.describe()} — "
            f"car wheels: {Car.wheels(self)}, bike wheels: {Bike.wheels(self)}"
        )


if __name__ == "__main__":
    g = GarageSale()
    print(g.describe())
    print(f"Car.wheels via MRO: {g.wheels()}")
    print(g.listing())
    print("MRO:", [c.__name__ for c in GarageSale.__mro__])
