# Command interface
class Command:
    def execute(self):
        pass


# Concrete Command 1
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.switch_on()


# Concrete Command 2
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.switch_off()


# Receiver
class Light:
    def switch_on(self):
        print("The light is on")

    def switch_off(self):
        print("The light is off")


# Invoker
class Switch:
    def __init__(self):
        self.commands = {}

    def register(self, command_name, command):
        self.commands[command_name] = command

    def execute(self, command_name):
        self.commands[command_name].execute()


# Usage
light = Light()
light_on_command = LightOnCommand(light)
light_off_command = LightOffCommand(light)

switch = Switch()
switch.register("on", light_on_command)
switch.register("off", light_off_command)

switch.execute("on")  # Output: The light is on
switch.execute("off")  # Output: The light is off
switch.execute("off")  # Output: The light is off
