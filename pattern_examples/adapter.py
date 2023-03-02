"""
Suppose you have an existing class that performs calculations in feet, but you need to use this class in a project
that works with meters. You could create an adapter class that converts the feet measurements to meters,
so that you can use the existing class without modifying it.
"""


# Existing class that performs calculations in feet
class FeetCalculator:
    def calculate_area(self, length_feet, width_feet):
        return length_feet * width_feet


# Adapter class that converts feet measurements to meters
class MetersAdapter:
    def __init__(self, calculator):
        self.calculator = calculator

    def calculate_area(self, length_meters, width_meters):
        length_feet = length_meters / 0.3048  # 1 meter = 0.3048 feet
        width_feet = width_meters / 0.3048
        return self.calculator.calculate_area(length_feet, width_feet)


# Usage
calculator = FeetCalculator()
adapter = MetersAdapter(calculator)
area_meters = adapter.calculate_area(10, 20)
print(area_meters)
