"""
The Abstract Factory design pattern is a creational pattern that provides an interface for creating families of related
or dependent objects without specifying their concrete classes. It allows the client to create objects of a family
without having to know the specific implementation details.
"""


# Abstract Factory
class DeviceComponentFactory:
    def create_display(self):
        pass

    def create_battery(self):
        pass

    def create_processor(self):
        pass


# Concrete Factories
class SmartphoneComponentFactory(DeviceComponentFactory):
    def create_display(self):
        return SmartphoneDisplay()

    def create_battery(self):
        return SmartphoneBattery()

    def create_processor(self):
        return SmartphoneProcessor()


class TabletComponentFactory(DeviceComponentFactory):
    def create_display(self):
        return TabletDisplay()

    def create_battery(self):
        return TabletBattery()

    def create_processor(self):
        return TabletProcessor()


class LaptopComponentFactory(DeviceComponentFactory):
    def create_display(self):
        return LaptopDisplay()

    def create_battery(self):
        return LaptopBattery()

    def create_processor(self):
        return LaptopProcessor()


class SmartwatchComponentFactory(DeviceComponentFactory):
    def create_display(self):
        return SmartwatchDisplay()

    def create_battery(self):
        return SmartwatchBattery()

    def create_processor(self):
        return SmartwatchProcessor()


# Abstract Products
class Display:
    def test_display(self):
        pass


class Battery:
    def test_battery(self):
        pass


class Processor:
    def test_processor(self):
        pass


# Concrete Products
class SmartphoneDisplay(Display):
    def test_display(self):
        print("Running smartphone display test...")


class SmartphoneBattery(Battery):
    def test_battery(self):
        print("Running smartphone battery test...")


class SmartphoneProcessor(Processor):
    def test_processor(self):
        print("Running smartphone processor test...")


class TabletDisplay(Display):
    def test_display(self):
        print("Running tablet display test...")


class TabletBattery(Battery):
    def test_battery(self):
        print("Running tablet battery test...")


class TabletProcessor(Processor):
    def test_processor(self):
        print("Running tablet processor test...")


class LaptopDisplay(Display):
    def test_display(self):
        print("Running laptop display test...")


class LaptopBattery(Battery):
    def test_battery(self):
        print("Running laptop battery test...")


class LaptopProcessor(Processor):
    def test_processor(self):
        print("Running laptop processor test...")


class SmartwatchDisplay(Display):
    def test_display(self):
        print("Running smartwatch display test...")


class SmartwatchBattery(Battery):
    def test_battery(self):
        print("Running smartwatch battery test...")


class SmartwatchProcessor(Processor):
    def test_processor(self):
        print("Running smartwatch processor test...")


# Usage
smartphone_factory = SmartphoneComponentFactory()
tablet_factory = TabletComponentFactory()
laptop_factory = LaptopComponentFactory()
smartwatch_factory = SmartwatchComponentFactory()

smartphone_display = smartphone_factory.create_display()
smartphone_display.test_display() # Output: Running smartphone display test...
smartphone_battery = smartphone_factory.create_battery()
smartphone_battery.test_battery() # Output: Running smartphone battery test...
smartphone_processor = smartphone_factory.create_processor()
smartphone_processor.test_processor() # Output: Running smartphone processor test...

tablet_display = tablet_factory.create_display()
tablet_display.test_display() # Output: Running tablet display test...
tablet_battery = tablet_factory.create_battery()
tablet_battery.test_battery() # Output: Running tablet battery test...
tablet_processor = tablet_factory.create_processor()
tablet_processor.test_processor() # Output: Running tablet processor test...

laptop_display = laptop_factory.create_display()
laptop_display.test_display() # Output: Running laptop display test...
laptop_battery = laptop_factory.create_battery()
laptop_battery.test_battery() # Output: Running laptop battery test...
laptop_processor = laptop_factory.create_processor()
laptop_processor.test_processor() # Output: Running laptop processor test...

smartwatch_display = smartwatch_factory.create_display()
smartwatch_display.test_display() # Output: Running laptop display test...
smartwatch_battery = smartwatch_factory.create_battery()
smartwatch_battery.test_battery() # Output: Running laptop battery test...
smartwatch_processor = smartwatch_factory.create_processor()
smartwatch_processor.test_processor() # Output: Running laptop processor test...

