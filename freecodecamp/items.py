import csv

class Item:
    # class attributes
    pay_rate = 0.82
    all = []

    def __init__(self, name, price: float, quantity: int):
        assert price >= 0, f'Price {price} is not greater than 0'
        assert quantity >= 0, f'Quantity {quantity} is not greater than 0'

        # instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # access the class attribute from the instance level
        return self.price

    @classmethod    # convert class method(function) to class objects
    def instantiate_from_class(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point 0
        # e.g 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        #return f'{self.name} costs ${self.price}'


print(Item.is_integer(6))
Item.instantiate_from_class()
print(Item.all)
'''
item1 = Item('Phone', 100, 5)       # instance of Item class
item2 = Item('Laptop', 7000, 9)     # instance of Item class

item3 = Item('Cable', 50, 6)
item4 = Item('House', 42, 3)
item5 = Item('Keyboard', 88, 12)

#print(item1.calculate_total_price())
#print(item1.price)
#print(item1.apply_discount())
#print(item1.price)
#print()
#print(Item.__dict__)
item2.pay_rate = 0.55
#print(item2.apply_discount())

print(Item.all)
for instance in Item.all:
    print(instance.name)
'''