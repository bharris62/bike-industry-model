class PriceRange:
    def __init__(self, money, bikes):
        self.money = money
        self.bikes = bikes

    def list(self):
        budget_bikes = []
        for bike in self.bikes:
            if self.money >= bike.price():
                budget_bikes.append(bike)

        return budget_bikes


