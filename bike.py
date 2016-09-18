class Bike(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def price(self):
        return self.cost * 1.20
