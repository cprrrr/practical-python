

from typedproperty import typedproperty, String, Integer, Float
class Stock:

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    @property
    def cost(self):
        return self.shares * self.price


    def sell(self, num : int):
        if num <= self.shares:
            self.shares -= int(num)
        else:
            print("dont have enough shares to sell")

