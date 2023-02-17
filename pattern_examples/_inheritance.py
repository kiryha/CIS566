"""
Public methods are the ones that can be accessed by anyone and are typically used for interaction with the object
_Protected methods are the ones that can be accessed within the class and its subclasses
__Private methods cannot be accessed outside the class and are used for internal implementation details
"""


# Parent | Superclass | Base
class Person(object):  # (object) no needed if no super() used in child classes
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


# Child | Subclass | Derived
class Teacher(Person):
    pass


class Student(Person):
    def __init__(self, name, height):
        Person.__init__(self, name)
        self.height = height


class Customer(Person):
    def __init__(self, name, value):
        super(Customer, self).__init__(name)
        self.value = value

    def print_name(self):
        super(Customer, self).print_name()
        print('Value: ', self.value)


teacher = Teacher('Kim')
teacher.print_name()

student = Student('Kiryha', 180)
student.print_name()

customer = Customer('Artem', 3678)
customer.print_name()

# Kim
# Kiryha
# Artem
# Value:  3678
