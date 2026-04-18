class products:
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
    def display(self):
        print(self.item, self.price, self.quantity)

p1 = products("Laptop", 50000, 10)
p1.display()


p2 = products("Mobile", 20000, 20)
p2.display()