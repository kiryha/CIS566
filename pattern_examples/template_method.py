from abc import ABC, abstractmethod


class AbstractRecipe(ABC):
    def prepare_recipe(self):
        self.gather_ingredients()
        self.preheat_oven()
        self.prepare_dish()
        self.cook()
        self.serve()

    @abstractmethod
    def gather_ingredients(self):
        pass

    def preheat_oven(self):
        print("Preheating the oven to 350°F.")

    @abstractmethod
    def prepare_dish(self):
        pass

    def cook(self):
        print("Cooking the dish in the oven.")

    def serve(self):
        print("Serving the dish.")


class PizzaRecipe(AbstractRecipe):
    def gather_ingredients(self):
        print("Gathering ingredients: pizza dough, tomato sauce, cheese, and toppings.")

    def prepare_dish(self):
        print("Rolling out the dough, adding sauce, cheese, and toppings.")


class BrownieRecipe(AbstractRecipe):
    def gather_ingredients(self):
        print("Gathering ingredients: chocolate, butter, sugar, eggs, and flour.")

    def prepare_dish(self):
        print("Melting chocolate and butter, mixing in sugar, eggs, and flour.")


pizza = PizzaRecipe()
print("Pizza Recipe:")
pizza.prepare_recipe()

print("\nBrownie Recipe:")
brownie = BrownieRecipe()
brownie.prepare_recipe()
