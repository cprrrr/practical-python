
class Stock:
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        if value < 0:
            raise ValueError('Expected positive')
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price


    def sell(self, num : int):
        if num <= self.shares:
            self.shares -= int(num)
        else:
            print("dont have enough shares to sell")

