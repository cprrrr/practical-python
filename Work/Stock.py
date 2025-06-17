
class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def cost(self):
        c = self.shares * self.price
        return c

    def sell(self, num : int):
        if num <= self.shares:
            self.shares -= int(num)
        else:
            print("dont have enough shares to sell")

