class Shop(object):
    def __init__(self, name):
        self.name = name
        self.bikes = []
        self.revenue = 0
        # TODO make a constant

    def stock_bikes(self, bikes):
        self.bikes = bikes

    def sell(self, bike):
        self.revenue += bike.price()
        self.bikes.remove(bike)

    def profit(self):
        pass
