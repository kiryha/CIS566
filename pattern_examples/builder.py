"""
The Builder pattern is a creational design pattern that allows you to separate the construction of complex objects
from their representation, so that the same construction process can create different representations.
"""


class Airplane:
    def __init__(self):
        self.model = None
        self.engine = None
        self.wingspan = None
        self.maximum_speed = None
        self.range = None
        self.capacity = None


class AirplaneBuilder:
    def __init__(self):
        self.airplane = Airplane()

    def build_model(self):
        pass

    def build_engine(self):
        pass

    def build_wingspan(self):
        pass

    def build_maximum_speed(self):
        pass

    def build_range(self):
        pass

    def build_capacity(self):
        pass

    def get_airplane(self):
        return self.airplane


class CropDuster(AirplaneBuilder):
    def build_model(self):
        self.airplane.model = "Crop Duster"

    def build_engine(self):
        self.airplane.engine = "Radial engine"

    def build_wingspan(self):
        self.airplane.wingspan = 10

    def build_maximum_speed(self):
        self.airplane.maximum_speed = 200

    def build_range(self):
        self.airplane.range = 200

    def build_capacity(self):
        self.airplane.capacity = 1


class FighterJet(AirplaneBuilder):
    def build_model(self):
        self.airplane.model = "Fighter Jet"

    def build_engine(self):
        self.airplane.engine = "Jet engine"

    def build_wingspan(self):
        self.airplane.wingspan = 35

    def build_maximum_speed(self):
        self.airplane.maximum_speed = 1500

    def build_range(self):
        self.airplane.range = 1200

    def build_capacity(self):
        self.airplane.capacity = 1


class Glide(AirplaneBuilder):
    def build_model(self):
        self.airplane.model = "Glider"

    def build_engine(self):
        self.airplane.engine = "None"

    def build_wingspan(self):
        self.airplane.wingspan = 25

    def build_maximum_speed(self):
        self.airplane.maximum_speed = 100

    def build_range(self):
        self.airplane.range = 400

    def build_capacity(self):
        self.airplane.capacity = 1


class AerospaceEngineer:
    def __init__(self, builder):
        self.builder = builder

    def construct_airplane(self):
        self.builder.build_model()
        self.builder.build_engine()
        self.builder.build_wingspan()
        self.builder.build_maximum_speed()
        self.builder.build_range()
        self.builder.build_capacity()

    def get_airplane(self):
        return self.builder.get_airplane()


# Example usage
builder = FighterJet()
engineer = AerospaceEngineer(builder)
engineer.construct_airplane()
airplane = engineer.get_airplane()
print(f"Model: {airplane.model}, Engine: {airplane.engine}, Wingspan: {airplane.wingspan}, Maximum Speed: {airplane.maximum_speed}, Range: {airplane.range}, Capacity: {airplane.capacity}")
