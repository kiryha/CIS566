from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            self._component2.react_on_a()
        elif event == "B":
            self._component1.react_on_b()


class BaseComponent:
    def __init__(self, mediator=None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator


class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 triggers event A.")
        self.mediator.notify(self, "A")

    def react_on_b(self):
        print("Component 1 reacts on event B.")


class Component2(BaseComponent):
    def do_b(self):
        print("Component 2 triggers event B.")
        self.mediator.notify(self, "B")

    def react_on_a(self):
        print("Component 2 reacts on event A.")


component1 = Component1()
component2 = Component2()
mediator = ConcreteMediator(component1, component2)

print("Client triggers operation A.")
component1.do_a()

print("\nClient triggers operation B.")
component2.do_b()
