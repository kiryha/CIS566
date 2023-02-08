"""
Class Project 1
CIS 476/566 Software Architecture and Design patterns
"""

import os


class AbstractDevice():
    def create_display(self):
        pass

    def create_battery(self):
        pass

    def create_processor(self):
        pass


class Smartphone(AbstractDevice):
    def create_display(self):
        return SmartphoneDisplay()

    def create_battery(self):
        return SmartphoneBattery()

    def create_processor(self):
        return SmartphoneProcessor()


class Tablet(AbstractDevice):
    def create_display(self):
        return TabletDisplay()

    def create_battery(self):
        return TabletBattery()

    def create_processor(self):
        return TabletProcessor()


class Laptop(AbstractDevice):
    def create_display(self):
        return LaptopDisplay()

    def create_battery(self):
        return LaptopBattery()

    def create_processor(self):
        return LaptopProcessor()


class Smartwatch(AbstractDevice):
    def create_display(self):
        return SmartwatchDisplay()

    def create_battery(self):
        return SmartwatchBattery()

    def create_processor(self):
        return SmartwatchProcessor()


class AbstractDisplay():
    def display_test(self):
        pass


class SmartphoneDisplay(AbstractDisplay):
    def display_test(self):
        return "Running Smartphone Display Test..."


class TabletDisplay(AbstractDisplay):
    def display_test(self):
        return "Running Tablet Display Test..."


class LaptopDisplay(AbstractDisplay):
    def display_test(self):
        return "Running Laptop Display Test..."


class SmartwatchDisplay(AbstractDisplay):
    def display_test(self):
        return "Running Smartwatch Display Test..."


class AbstractBattery():
    def battery_test(self):
        pass


class SmartphoneBattery(AbstractBattery):
    def battery_test(self):
        return "Running Smartphone Battery Test..."


class TabletBattery(AbstractBattery):
    def battery_test(self):
        return "Running Tablet Battery Test..."


class LaptopBattery(AbstractBattery):
    def battery_test(self):
        return "Running Laptop Battery Test..."


class SmartwatchBattery(AbstractBattery):
    def battery_test(self):
        return "Running Smartwatch Battery Test..."


class AbstractProcessor():
    def processor_test(self):
        pass


class SmartphoneProcessor(AbstractProcessor):
    def processor_test(self):
        return "Running Smartphone Processor Test..."


class TabletProcessor(AbstractProcessor):
    def processor_test(self):
        return "Running Tablet Processor Test..."


class LaptopProcessor(AbstractProcessor):
    def processor_test(self):
        return "Running Laptop Processor Test..."


class SmartwatchProcessor(AbstractProcessor):
    def processor_test(self):
        return "Running Smartwatch"


class Test:
    def __init__(self):
        self.devices = None
        self.run_test()

    def run_test(self):

        root = os.path.dirname(os.path.abspath(__file__))
        with open('{0}/devices.txt'.format(root), 'r') as file:
            self.devices = file.read().split('\n')

        for class_name in self.devices:
            print '>> Current device is {}'.format(class_name)
            device = None
            device = eval('{}()'.format(class_name))
            display = device.create_display()
            battery = device.create_battery()
            processor = device.create_processor()
            print("{0}\n{1}\n{2}".format(display.display_test(), battery.battery_test(), processor.processor_test()))


if __name__ == "__main__":

    Test()
