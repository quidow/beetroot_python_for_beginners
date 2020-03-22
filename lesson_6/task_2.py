"""
Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock.
"""


def total_price(list_1, list_2):
    total = 0
    for key in list_1:
        price = list_1[key] * list_2.get(key, 0)
        total += price
    return total


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print(total_price(stock, prices))

