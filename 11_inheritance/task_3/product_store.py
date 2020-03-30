from decimal import *


class Product:

    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:

    def __init__(self):
        self.products = []
        self.income = Decimal(0).quantize(Decimal('.01'))

    def add(self, product, amount):
        if not isinstance(product, Product) and not isinstance(amount, int):
            raise TypeError
        for p in self.products:
            if p["name"] == product.name and p["type"] == product.type:
                p["price"] = Decimal(product.price * 1.3).quantize(Decimal('.01'), rounding=ROUND_UP)
                p["amount"] += amount
                break
        else:
            self.products.append({
                "type": product.type,
                "name": product.name,
                "price": Decimal(product.price * 1.3).quantize(Decimal('.01'), rounding=ROUND_UP),
                "amount": amount
            })

    def set_discount(self, identifier, percent, identifier_type='name'):
        if not 0 <= percent <= 1:
            raise ValueError
        for p in self.products:
            if p[identifier_type] == identifier:
                p["price"] -= Decimal(p["price"] * Decimal(percent)).quantize(Decimal('.01'), rounding=ROUND_DOWN)

    def sell_product(self, product_name, amount):
        if not isinstance(amount, int):
            raise TypeError
        for p in self.products:
            if p["name"] == product_name:
                if p["amount"] < amount:
                    raise ValueError
                else:
                    p["amount"] -= amount
                    self.income += p["price"] * amount

    def get_income(self):
        return float(self.income)

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        for p in self.products:
            if p["name"] == product_name:
                return p["name"], p["amount"]
