# Model
class Model:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def remove_item(self, item):
        self.data.remove(item)

    def get_data(self):
        return self.data


# View
class View:
    def display_items(self, items):
        print("Items in the list:")
        for item in items:
            print(item)

    def get_item_input(self):
        return input("Enter an item: ")

    def get_item_to_remove(self):
        return input("Enter the item to remove: ")


# Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_item(self):
        item = self.view.get_item_input()
        self.model.add_item(item)
        self.view.display_items(self.model.get_data())

    def remove_item(self):
        item = self.view.get_item_to_remove()
        self.model.remove_item(item)
        self.view.display_items(self.model.get_data())


model = Model()
view = View()
controller = Controller(model, view)

while True:
    action = input("Enter 'add' to add an item, 'remove' to remove an item, or 'quit' to exit: ")
    if action == 'add':
        controller.add_item()
    elif action == 'remove':
        controller.remove_item()
    elif action == 'quit':
        break
    else:
        print("Invalid input, please try again.")
