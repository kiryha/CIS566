from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class SimpleCoffee(Coffee):
    def get_cost(self):
        return 4.0

    def get_description(self):
        return 'Black Coffee'


class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def get_cost(self):
        return self._coffee.get_cost()

    def get_description(self):
        return self._coffee.get_description()


class Latte(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return super().get_cost() + 4.5

    def get_description(self):
        return super().get_description() + ', Latte'


class Muffin(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return super().get_cost() + 1.3

    def get_description(self):
        return super().get_description() + ', Muffin'


class Butter(CoffeeDecorator):
    def __init__(self, coffee, percentage):
        super().__init__(coffee)
        self._percentage = percentage

    def get_cost(self):
        return super().get_cost() + (self._percentage / 100) * 1.2

    def get_description(self):
        return super().get_description() + f', Butter ({self._percentage}%)'


class Coupon(CoffeeDecorator):
    _instance = None

    def __init__(self, coffee):
        if Coupon._instance is not None:
            raise Exception("Singleton class can't be instantiated more than once.")
        super().__init__(coffee)
        Coupon._instance = self

    def get_cost(self):
        return super().get_cost() * 0.9

    def get_description(self):
        return super().get_description() + ', 10% Off'


order = SimpleCoffee()
order = Latte(order)
order = Butter(order, 50)
order = Muffin(order)
order = Muffin(order)
order = Coupon(order)

print(f'Item: {order.get_description()}')
print(f'Cost: ${order.get_cost():.2f}')
