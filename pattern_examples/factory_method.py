"""
Factory Method

The Factory Method pattern is a creational pattern that provides an interface for creating objects in a super class,
but allows subclasses to alter the type of objects that will be created.

The idea is to delegate the responsibility of object creation to subclasses, rather than the client code,
which enhances the flexibility of the software design.

# Simplified version
class CheesePizza:
    def prepare(self):
        print("Preparing cheese pizza...")

    def __str__(self):
        return "Cheese Pizza"


class PepperoniPizza:
    def prepare(self):
        print("Preparing pepperoni pizza...")

    def __str__(self):
        return "Pepperoni Pizza"


class OrderPizza:
    def order_pizza(self, pizza_type: str):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        print(f"Here's your {pizza}! Enjoy!")
        return pizza

    def create_pizza(self, pizza_type: str):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()


# Order Simplified
order_pizza = OrderPizza()
cheese_pizza = order_pizza.order_pizza("cheese")
pepperoni_pizza = order_pizza.order_pizza("pepperoni")
"""


# Full pattern
class Pizza:
    def prepare(self):
        pass

    def box(self):
        pass


class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing cheese pizza...")

    def box(self):
        print("Packing cheese pizza...")

    def __str__(self):
        return "Cheese Pizza"


class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing pepperoni pizza...")

    def box(self):
        print("Packing pepperoni pizza...")

    def __str__(self):
        return "Pepperoni Pizza"


class PizzaStore:
    def create_pizza(self, pizza_type):
        raise NotImplementedError()

    def order_pizza(self, pizza_type):

        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()


ny_store = NYPizzaStore()
cheese_pizza = ny_store.order_pizza("cheese")
pepperoni_pizza = ny_store.order_pizza("pepperoni")
