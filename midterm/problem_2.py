from abc import ABC, abstractmethod


class Coffee(ABC):
    def __init__(self, size, sugar, cream):
        self.size = size
        self.sugar = sugar
        self.cream = cream

    @abstractmethod
    def get_type(self):
        pass

    def get_size(self):
        return self.size

    def get_sugar(self):
        return self.sugar

    def get_cream(self):
        return self.cream


class Latte(Coffee):
    def __init__(self, size, sugar, cream):
        super().__init__(size, sugar, cream)
        self.type = "Latte"

    def get_type(self):
        return self.type


class Cappuccino(Coffee):
    def __init__(self, size, sugar, cream):
        super().__init__(size, sugar, cream)
        self.type = "Cappuccino"

    def get_type(self):
        return self.type


class CoffeeFactory:
    def create_coffee(self, order):
        if order == 1:
            return Latte("Medium", "No sugar", "Extra shot")
        elif order == 2:
            return Cappuccino("Small", "1 sugar", "No cream")
        else:
            raise ValueError("Invalid order number")


if __name__ == "__main__":
    print("Welcome, what would you like to order? Please choose 1 or 2.")
    order_number = int(input())

    factory = CoffeeFactory()
    coffee = factory.create_coffee(order_number)

    print(f"Order {order_number}:")
    print(f"Type: {coffee.get_type()}")
    print(f"Size: {coffee.get_size()}")
    print(f"Extras: {coffee.get_sugar()}, {coffee.get_cream()}")
