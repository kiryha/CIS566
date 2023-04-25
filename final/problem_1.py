from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Concrete command classes
class MakeBurgerCommand(Command):
    def __init__(self, chef):
        self._chef = chef

    def execute(self):
        self._chef.make_food("Burger")


class MakeSandwichCommand(Command):
    def __init__(self, chef):
        self._chef = chef

    def execute(self):
        self._chef.make_food("Sandwich")


# Receiver classes
class Chef:
    def make_food(self, food):
        print(f"Chef {self.__class__.__name__} is making a {food}.")


class ChefA(Chef):
    pass


class ChefB(Chef):
    pass


# Invoker class
class Waitress:
    def __init__(self, chef_a, chef_b):
        self._chef_a = chef_a
        self._chef_b = chef_b

    def take_order(self, food):
        if food == "B":
            command = MakeBurgerCommand(self._chef_a)
        elif food == "S":
            command = MakeSandwichCommand(self._chef_b)
        else:
            raise ValueError("Invalid food item.")

        command.execute()


# Client code
chef_a = ChefA()
chef_b = ChefB()
waitress = Waitress(chef_a, chef_b)

print("Welcome, would you like to order a burger (B) or sandwich (S)?")
customer_choice = input().strip()
waitress.take_order(customer_choice)
