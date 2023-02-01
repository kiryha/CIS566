"""
In this example, we have three classes: State, ConcreteStateA, and ConcreteStateB.
The State class is an interface that defines the handle method, which will be implemented by the concrete state classes.
ConcreteStateA and ConcreteStateB are concrete implementations of the state interface,
and define the behavior of the object in their respective states.

The Context class contains a reference to the current state of the object and implements the handle method,
which delegates the request to the current state's handle method.
The context's state can be changed at runtime by calling the set_state method.
"""


class State:
    def handle(self, context):
        pass


class ConcreteStateA(State):
    def handle(self, context):
        print("Handling request in state A")
        context.set_state(ConcreteStateB())


class ConcreteStateB(State):
    def handle(self, context):
        print("Handling request in state B")
        context.set_state(ConcreteStateA())


class Context:
    def __init__(self):
        self._state = ConcreteStateA()

    def set_state(self, state):
        self._state = state

    def handle(self):
        self._state.handle(self)


context = Context()
context.handle()
context.handle()
context.handle()
