# class Products, serialization and deserialization
import json
from random import randint

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}'


product1 = Product('Phone', randint(10, 100), randint(1, 10))
product2 = Product('Laptop', randint(10, 100), randint(1, 10))
product3 = Product('Watch', randint(10, 100), randint(1, 10))
product4 = Product('Scroll', randint(10, 100), randint(1, 10))
product5 = Product('Tablet', randint(10, 100), randint(1, 10))
product6 = Product('Speaker', randint(10, 100), randint(1, 10))
product7 = Product('Headphones', randint(10, 100), randint(1, 10))

products = [product1, product2, product3, product4, product5, product6, product7]


def custom_serializer(obj):
    if isinstance(obj, Product):
        return {'name': obj.name, 'price': obj.price, 'quantity': obj.quantity}
    
    raise TypeError('Object must be of type Product')



with open ('products.json', 'w') as json_file:
    json.dump(products, json_file, default=custom_serializer, indent=4)



def custom_deserializer(json_obj):
    return Product(json_obj['name'], json_obj['price'], json_obj['quantity'])



with open ('products.json', 'r') as json_file:
    json_products = json.load(json_file, object_hook=custom_deserializer)
    print(json_products)

for product in json_products:
    print(product)