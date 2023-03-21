"""
class SortingStrategy:
    def sort(self, data):
        pass


class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        # Implementation of bubble sort
        return sorted(data)


class MergeSortStrategy(SortingStrategy):
    def sort(self, data):
        # Implementation of merge sort
        return sorted(data)


class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        # Implementation of quick sort
        return sorted(data)


class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)


data = [4, 2, 7, 1, 3, 5]


sorter = Sorter(BubbleSortStrategy())
print(sorter.sort(data))  # Output: [1, 2, 3, 4, 5, 7]

sorter.set_strategy(QuickSortStrategy())
print(sorter.sort(data))  # Output: [1, 2, 3, 4, 5, 7]
"""


# Abstract class for all types of ducks
class Duck:
    def __init__(self, quack_strategy, fly_strategy):
        self.quack_strategy = quack_strategy
        self.fly_strategy = fly_strategy

    def swim(self):
        print("All ducks float, even decoys!")

    def display(self):
        pass

    def quack(self):
        self.quack_strategy.quack()

    def fly(self):
        self.fly_strategy.fly()


# Abstract class for all quack strategies
class QuackStrategy:
    def quack(self):
        pass


# Concrete implementation of quack strategy for quack ducks
class Quack(QuackStrategy):
    def quack(self):
        print("Quack")


# Concrete implementation of quack strategy for squeak ducks
class Squeak(QuackStrategy):
    def quack(self):
        print("Squeak")


# Concrete implementation of quack strategy for mute ducks
class MuteQuack(QuackStrategy):
    def quack(self):
        print("<< Silence >>")


# Abstract class for all fly strategies
class FlyStrategy:
    def fly(self):
        pass


# Concrete implementation of fly strategy for ducks that can fly
class FlyWithWings(FlyStrategy):
    def fly(self):
        print("I'm flying with wings!")


# Concrete implementation of fly strategy for ducks that can't fly
class FlyNoWay(FlyStrategy):
    def fly(self):
        print("I can't fly :(")


# Concrete implementation of fly strategy for ducks that use a rocket to fly
class FlyRocketPowered(FlyStrategy):
    def fly(self):
        print("I'm flying with a rocket!")


# Concrete implementation of Duck for Mallard ducks
class MallardDuck(Duck):
    def __init__(self):
        super().__init__(Quack(), FlyWithWings())

    def display(self):
        print("I'm a real Mallard duck")


# Concrete implementation of Duck for Rubber ducks
class RubberDuck(Duck):
    def __init__(self):
        super().__init__(Squeak(), FlyNoWay())

    def display(self):
        print("I'm a rubber duckie")


# Concrete implementation of Duck for Decoy ducks
class DecoyDuck(Duck):
    def __init__(self):
        super().__init__(MuteQuack(), FlyNoWay())

    def display(self):
        print("I'm a wooden decoy duck")


# Example usage
mallard = MallardDuck()
mallard.display()
mallard.quack()
mallard.fly()

rubber_duck = RubberDuck()
rubber_duck.display()
rubber_duck.quack()
rubber_duck.fly()

decoy = DecoyDuck()
decoy.display()
decoy.quack()
decoy.fly()

