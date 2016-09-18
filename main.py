from customer import Customer
from shop import Shop
from bike import Bike
from price_range import PriceRange


def main():
    inventory = [Bike('Huffy', 20, 100),
                 Bike('Shwynn', 25, 200),
                 Bike('Standard', 30, 300),
                 Bike('Mtn Bk', 35, 400),
                 Bike('Pro', 40, 500),
                 Bike('Walmart', 45, 600)]

    shop = Shop('Bike Shop')
    shop.stock_bikes(inventory)

    customers = [Customer('Blake', 200),
                Customer('Austin', 500),
                Customer('Michael', 1000)]

    for customer in customers:
        print("{}, you have ${}".format(customer.name, customer.money))
        for bike in PriceRange(customer.money, shop.bikes).list():
            print("     {}: ${}".format(bike.name, bike.price()))

    for customer in customers:
        customer.buy(shop, PriceRange(customer.money, shop.bikes).list()[0])
        print("{} bought {} for ${}".format(customer.name, customer.bike.name, customer.bike.price()))


if __name__ == '__main__':
    main()
