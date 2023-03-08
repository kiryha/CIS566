class Coffee:
    def __init__(self):
        self._type = None
        self._size = None
        self._sugar = False
        self._cream = False
        self._extra_shot = False

    def __str__(self):
        extras = []
        if self._sugar:
            extras.append("Sugar")
        else:
            extras.append("No Sugar")
        if self._cream:
            extras.append("Cream")
        else:
            extras.append("No Cream")
        if self._extra_shot:
            extras.append("extra shot")
        else:
            extras.append("No Extra Shot")

        return f"Type: {self._type}\nSize {self._size.capitalize()}\nExtras: {extras}\n\n"


class CoffeeBuilder:
    def __init__(self):
        self._coffee = Coffee()

    def set_type(self, coffee_type):
        self._coffee._type = coffee_type

    def set_size(self, size):
        self._coffee._size = size

    def add_sugar(self):
        self._coffee._sugar = True

    def add_cream(self):
        self._coffee._cream = True

    def add_extra_shot(self):
        self._coffee._extra_shot = True

    def get_coffee(self):
        return self._coffee


class Barista:
    def __init__(self):
        self._builder = None

    def set_builder(self, builder):
        self._builder = builder

    def construct_coffee(self, coffee_type, size, extras):
        self._builder.set_type(coffee_type)
        self._builder.set_size(size)
        for extra in extras:
            if extra == "sugar":
                self._builder.add_sugar()
            elif extra == "cream":
                self._builder.add_cream()
            elif extra == "extra shot":
                self._builder.add_extra_shot()


if __name__ == "__main__":

    # Order 1: Latte, medium, no sugar, extra shot
    builder_1 = CoffeeBuilder()
    barista_1 = Barista()
    barista_1.set_builder(builder_1)
    barista_1.construct_coffee("Latte", "medium", ["extra shot"])
    coffee_1 = builder_1.get_coffee()

    # Order 2: Cappuccino, small, extra sugar, no cream
    builder_2 = CoffeeBuilder()
    barista_2 = Barista()
    barista_2.set_builder(builder_2)
    barista_2.construct_coffee("Cappuccino", "small", ["sugar"])
    coffee_2 = builder_2.get_coffee()

    print('Order 1:\n')
    print(coffee_1)
    print('Order 2:\n')
    print(coffee_2)
