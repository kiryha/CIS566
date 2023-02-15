"""
In this example, we start by defining the Beverage parent class, which has a get_description method that returns the
description of the beverage and a cost method that returns the cost of the beverage. We then define three child classes,
Coffee, Tea, and Water, that inherit from Beverage and implement their own versions of the get_description and cost methods.

We then define the CondimentDecorator class, which is a subclass of Beverage and wraps another Beverage instance.
This class doesn't implement its own get_description or cost methods,
but delegates those methods to the wrapped Beverage instance.

We then define two subclasses of CondimentDecorator, Sugar and Milk, which add sugar and milk to a Beverage instance
respectively. These classes override the get_description and cost methods of CondimentDecorator to add their own
description and cost, as well as delegate the same methods to the wrapped Beverage instance.

Finally, we create a Coffee instance and wrap it with a Sugar and a Milk instance using the decorator pattern.
We then print the description and cost of the resulting Beverage instance, which includes the added sugar and milk.
"""


# Base Item
class Beverage:
    def __init__(self):
        self.description = "Abstract Beverage"

    def get_description(self):
        return self.description

    def cost(self):
        pass


# Condiment decorator
class CondimentDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        pass


# Base Item options
class Coffee(Beverage):
    def __init__(self):
        self.description = "Coffee"

    def cost(self):
        return 3


class Tea(Beverage):
    def __init__(self):
        self.description = "Tea"

    def cost(self):
        return 2


class Water(Beverage):
    def __init__(self):
        self.description = "Water"

    def cost(self):
        return 1


# Condiment options
class Sugar(CondimentDecorator):
    def get_description(self):
        return self.beverage.get_description() + " + Sugar"

    def cost(self):
        return self.beverage.cost() + 0.2


class Milk(CondimentDecorator):
    def get_description(self):
        return self.beverage.get_description() + " + Milk"

    def cost(self):
        return self.beverage.cost() + 0.3


# Use the decorators to modify the behavior of the Beverages
beverage = Coffee()
beverage = Sugar(beverage)
beverage = Milk(beverage)

print (beverage.get_description() + " = $" + str(beverage.cost()))

# Coffee + Sugar + Milk = $3.5

