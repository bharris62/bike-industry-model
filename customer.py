class Customer(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bike = None

    def buy(self, shop, bike):
        self.money -= bike.cost
        shop.sell(bike)
        self.bike = bike
