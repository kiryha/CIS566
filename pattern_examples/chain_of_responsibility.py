"""
In this example, we define an abstract Handler class that defines a default implementation for handling requests,
and concrete ConcreteHandler classes that inherit from the Handler class and implement their own request handling logic.
We then create instances of the concrete handlers and set up the chain of responsibility by linking them together
with their set_successor() method.
Finally, we test the chain of responsibility by passing requests to the first handler in the chain (handler_a)
and checking if any of the handlers can handle the request. If a handler can handle the request, it returns a result.
If not, the request is passed on to the next handler in the chain until a suitable handler is found.
"""


# Define the abstract handler class
class Handler:
    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            return self._successor.handle(request)

        return None


# Define the concrete handler classes
class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == 'A':
            return f"{request} handled by ConcreteHandlerA"
        else:
            return super().handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == 'B':
            return f"{request} handled by ConcreteHandlerB"
        else:
            return super().handle(request)


class ConcreteHandlerC(Handler):
    def handle(self, request):
        if request == 'C':
            return f"{request} handled by ConcreteHandlerC"
        else:
            return super().handle(request)


# Create the chain of responsibility
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()
handler_c = ConcreteHandlerC()
handler_a.set_successor(handler_b)
handler_b.set_successor(handler_c)


# Test the chain of responsibility
requests = ['A', 'B', 'C', 'D']
for request in requests:
    result = handler_a.handle(request)
    if result:
        print(result)
    else:
        print(f"No handler found for {request}")
