"""
Class Project 1
CIS 476/566 Software Architecture and Design patterns
"""

import os


class AbstractFactory:
    def create_phone(self):
        pass

    def create_watch(self):
        pass

    def create_laptop(self):
        pass

    def create_tablet(self):
        pass



class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()



class ProductA:
    def feature(self):
        pass



class ProductA1(ProductA):
    def feature(self):
        return "Feature of Product A1"



class ProductA2(ProductA):
    def feature(self):
        return "Feature of Product A2"



class ProductB:
    def feature(self):
        pass



class ProductB1(ProductB):
    def feature(self):
        return "Feature of Product B1"



class ProductB2(ProductB):
    def feature(self):
        return "Feature of Product B2"



class RunTest:
    def __init__(self):
        self.devices = None

        self.read_data()

    def read_data(self):

        root = os.path.dirname(os.path.abspath(__file__))
        with open('{0}/devices.txt'.format(root), 'r') as file:
            self.devices = file.read().split('\n')

        print self.devices


def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        print(product_a.feature(), product_b.feature())


if __name__ == "__main__":

    # RunTest()
    main()
