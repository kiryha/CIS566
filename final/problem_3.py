"""
implement a Python application for a realtor to display the
properties. The realtor can enter and update house information and
customers can search and preview house for sale based on different criteria,
such as price range, city, zip, year built, property type, number of bedrooms.
You are required to use MVC pattern to implement the application.

Model
The model should include the following information for each house
• Price
• Address
• City
• Zip
• Year built
• Property type (single, condo, townhome)
• Number of bedrooms 28

Views
Create three views,
View 1: For realtor to enter and update house information
View 2: For customer to search and display search result list.
View 3: Detail view of the house when customer clicks on a house in the result
list in the view 2

Controller
Provides control and navigation among views in response to Form buttons,
pass data to and retrieve data from the Model classes. It should provide
function to support the following:
• Determine the desired operation in response to user’s input and demand
• Call the appropriate Model method to prepare the returned data for display
• Transfer data to the appropriate view.
"""


from PySide2 import QtCore, QtWidgets
from ui import ui_zillow

# Database ID counter
index = 0


# Model
class House:
    def __init__(self, price, address, city, zip_code, year_built, property_type, bedrooms):
        self.index = None
        self.price = price
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.year_built = year_built
        self.property_type = property_type
        self.bedrooms = bedrooms

        self.set_index()

    def set_index(self):
        global index
        self.index = index
        index += 1


class Model:
    def __init__(self):
        self.houses = []

    def add_house(self, price, address, city, zip_code, year_built, property_type, bedrooms):

        house = House(price, address, city, zip_code, year_built, property_type, bedrooms)
        self.houses.append(house)

        return house

    def update_house(self, index, house):

        self.houses[index] = house

    def search_houses(self, criteria):

        houses = []

        for house in self.houses:
            if self.matches_criteria(house, criteria):
                houses.append(house)

        return houses

    def get_house(self, index):
        return self.houses[index]

    def matches_criteria(self, house, criteria):

        for key, value in criteria.items():
            if getattr(house, key) != str(value):

                return False

        return True

    def get_search_criteria(self, price_range, city, zip_code, year_built, property_type, bedrooms):
        criteria = {}

        if price_range:
            low, high = map(int, price_range.split('-'))
            criteria['price'] = (low, high)

        if city:
            criteria['city'] = city

        if zip_code:
            criteria['zip_code'] = zip_code

        if year_built:
            criteria['year_built'] = int(year_built)

        if property_type:
            criteria['property_type'] = property_type

        if bedrooms:
            criteria['bedrooms'] = int(bedrooms)

        return criteria


# Views
class View1:
    @staticmethod
    def display_success(house):

        house_details = f"House of index {house.index} created!\n\n" \
                        f"Price: ${house.price}\nAddress: {house.address}\nCity: {house.city}\n" \
                        f"Zip: {house.zip_code}\nYear built: {house.year_built}\n" \
                        f"Property type: {house.property_type}\nBedrooms: {house.bedrooms}"

        return house_details


class View2:
    @staticmethod
    def display_search_results(houses):

        string = ''

        for i, house in enumerate(houses):
            print(f"{house.index}. {house.address}, {house.city}, {house.zip_code}")
            string += f"{house.index}. {house.address}, {house.city}, {house.zip_code}\n"

        return string


class View3:
    @staticmethod
    def display_house_details(house):

        house_details = f"Price: ${house.price}\nAddress: {house.address}\nCity: {house.city}\n" \
                        f"Zip: {house.zip_code}\nYear built: {house.year_built}\n" \
                        f"Property type: {house.property_type}\nBedrooms: {house.bedrooms}"

        return house_details


# Controller
class Zillow(QtWidgets.QMainWindow, ui_zillow.Ui_Zillow):

    def __init__(self, parent=None):
        super(Zillow, self).__init__(parent=parent)
        self.setupUi(self)

        # Create Data Model
        self.model = Model()

        # UI Calls
        self.btnClear.clicked.connect(self.clear_ui)
        self.btnAddHouse.clicked.connect(self.add_house)
        self.btnSearchHouse.clicked.connect(self.search_houses)

    def clear_ui(self):

        self.linPrice.setText('')
        self.linAddress.setText('')
        self.linCity.setText('')
        self.linZip.setText('')
        self.linYear.setText('')
        self.linType.setText('')
        self.linBedrooms.setText('')

    def add_house(self):

        # Get data from UI
        price = self.linPrice.text()
        address = self.linAddress.text()
        city = self.linCity.text()
        zip_code = self.linZip.text()
        year_built = self.linYear.text()
        property_type = self.linType.text()
        bedrooms = self.linBedrooms.text()

        # Create house
        house = self.model.add_house(price, address, city, zip_code, year_built, property_type, bedrooms)

        # Display Data
        message = View1.display_success(house)
        self.linResults.clear()
        self.linResults.append(message)

    def search_houses(self):

        # Get Data
        price = self.linPrice.text() if self.linPrice.text() != '' else None
        city = self.linCity.text() if self.linCity.text() != '' else None
        zip_code = self.linZip.text() if self.linZip.text() != '' else None
        year_built = self.linYear.text() if self.linYear.text() != '' else None
        property_type = self.linType.text() if self.linType.text() != '' else None
        bedrooms = self.linBedrooms.text() if self.linBedrooms.text() != '' else None

        # Search houses
        criteria = self.model.get_search_criteria(price, city, zip_code, year_built, property_type, bedrooms)
        filtered_houses = self.model.search_houses(criteria)

        # Display Data
        message = View2.display_search_results(filtered_houses)
        self.linResults.clear()
        self.linResults.append(message)


# Launch the Zillow application
app = QtWidgets.QApplication([])
zillow = Zillow()
zillow.show()
app.exec_()
