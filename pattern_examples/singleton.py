class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            print("This class is a Singleton and it already has an instance! Skipping creation")
            return
        else:
            Singleton.__instance = self

    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def say_hello(self):
        print("Hello from the Singleton!")


# Usage example
singleton1 = Singleton.get_instance()
singleton1.say_hello()

singleton2 = Singleton.get_instance()
singleton2.say_hello()

singleton3 = Singleton()

# Output:
# Hello from the Singleton!
# Hello from the Singleton!
