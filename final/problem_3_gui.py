from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QSpinBox, QPlainTextEdit, QTableWidget, QTableWidgetItem, QMessageBox, QWidget
from PySide2.QtCore import Qt

# Model
class House:
    def __init__(self, price, address, city, zip_code, year_built, property_type, bedrooms):
        self.price = price
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.year_built = year_built
        self.property_type = property_type
        self.bedrooms = bedrooms


class Model:
    def __init__(self):
        self.houses = []

    def add_house(self, house):
        self.houses.append(house)

    def update_house(self, index, house):
        self.houses[index] = house

    def search_houses(self, criteria):
        return [house for house in self.houses if self._matches_criteria(house, criteria)]

    def get_house(self, index):
        return self.houses[index]

    def _matches_criteria(self, house, criteria):
        for key, value in criteria.items():
            if getattr(house, key) != value:
                return False
        return True

from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QSpinBox, QPlainTextEdit, QTableWidget, QTableWidgetItem, QMessageBox, QWidget
from PySide2.QtCore import Qt

# Model and House classes remain the same

# Views and Controller
class View1(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Price
        hbox_price = QHBoxLayout()
        hbox_price.addWidget(QLabel("Price:"))
        self.price_input = QLineEdit()
        hbox_price.addWidget(self.price_input)
        layout.addLayout(hbox_price)

        # Address
        hbox_address = QHBoxLayout()
        hbox_address.addWidget(QLabel("Address:"))
        self.address_input = QLineEdit()
        hbox_address.addWidget(self.address_input)
        layout.addLayout(hbox_address)

        # City
        hbox_city = QHBoxLayout()
        hbox_city.addWidget(QLabel("City:"))
        self.city_input = QLineEdit()
        hbox_city.addWidget(self.city_input)
        layout.addLayout(hbox_city)

        # Zip
        hbox_zip = QHBoxLayout()
        hbox_zip.addWidget(QLabel("Zip:"))
        self.zip_input = QLineEdit()
        hbox_zip.addWidget(self.zip_input)
        layout.addLayout(hbox_zip)

        # Year built
        hbox_year_built = QHBoxLayout()
        hbox_year_built.addWidget(QLabel("Year built:"))
        self.year_built_input = QSpinBox()
        self.year_built_input.setRange(1800, 2100)
        hbox_year_built.addWidget(self.year_built_input)
        layout.addLayout(hbox_year_built)

        # Property type
        hbox_property_type = QHBoxLayout()
        hbox_property_type.addWidget(QLabel("Property type:"))
        self.property_type_input = QComboBox()
        self.property_type_input.addItems(["single", "condo", "townhome"])
        hbox_property_type.addWidget(self.property_type_input)
        layout.addLayout(hbox_property_type)

        # Bedrooms
        hbox_bedrooms = QHBoxLayout()
        hbox_bedrooms.addWidget(QLabel("Bedrooms:"))
        self.bedrooms_input = QSpinBox()
        self.bedrooms_input.setRange(1, 20)
        hbox_bedrooms.addWidget(self.bedrooms_input)
        layout.addLayout(hbox_bedrooms)

        # Buttons
        hbox_buttons = QHBoxLayout()
        add_button = QPushButton("Add House")
        add_button.clicked.connect(self.add_house)
        hbox_buttons.addWidget(add_button)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_inputs)
        hbox_buttons.addWidget(clear_button)
        layout.addLayout(hbox_buttons)

        self.setLayout(layout)

    def add_house(self):
        house_info = House(
            int(self.price_input.text()),
            self.address_input.text(),
            self.city_input.text(),
            self.zip_input.text(),
            self.year_built_input.value(),
            self.property_type_input.currentText(),
            self.bedrooms_input.value()
        )
        self.controller.add_house(house_info)
        QMessageBox.information(self, "Success", "House information added successfully.")
        self.clear_inputs()

    def clear_inputs(self):
        self.price_input.clear()
        self.address_input.clear()
        self.city_input.clear()
        self.zip_input.clear()
        self.year_built_input.setValue(1900)
        self.property_type_input.setCurrentIndex(0)
        self.bedrooms_input.setValue(1)


class View2(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Search button
        search_button = QPushButton("Search Houses")
        search_button.clicked.connect(self.search_houses)
        layout.addWidget(search_button)

        # Results table
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(3)
        self.results_table.setHorizontalHeaderLabels(["Address", "City", "Zip"])
        self.results_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.results_table.setSelectionMode(QTableWidget.SingleSelection)
        self.results_table.cellDoubleClicked.connect(self.show_house_details)
        layout.addWidget(self.results_table)

        self.setLayout(layout)

    def search_houses(self):
        self.results_table.setRowCount(0)
        filtered_houses = self.controller.search_houses()
        for house in filtered_houses:
            row = self.results_table.rowCount()
            self.results_table.insertRow(row)
            self.results_table.setItem(row, 0, QTableWidgetItem(house.address))
            self.results_table.setItem(row, 1, QTableWidgetItem(house.city))
            self.results_table.setItem(row, 2, QTableWidgetItem(house.zip_code))

    def show_house_details(self, row):
        house = self.controller.get_house(row)
        View3.display_house_details(house)


class View3:
    @staticmethod
    def display_house_details(house):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("House Details")
        msg.setText(
            f"Price: ${house.price}\n"
            f"Address: {house.address}\n"
            f"City: {house.city}\n"
            f"Zip: {house.zip_code}\n"
            f"Year built: {house.year_built}\n"
            f"Property type: {house.property_type}\n"
            f"Bedrooms: {house.bedrooms}"
        )
        msg.exec_()

class Controller:
    def __init__(self, model):
        self.model = model

    def add_update_house(self, index=None):
        house_info = View1.get_house_info()
        if index is None:
            self.model.add_house(house_info)
        else:
            self.model.update_house(index, house_info)
        View1.display_success()

    def search_houses(self):
        criteria = View2.get_search_criteria()
        filtered_houses = self.model.search_houses(criteria)
        View2.display_search_results(filtered_houses)
        return filtered_houses

    def display_house_details(self, index):
        house = self.model.get_house(index)
        View3.display_house_details(house)

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.setWindowTitle("Realtor Application")
        self.controller = controller

        # Create views
        self.view1 = View1(controller)
        self.view2 = View2(controller)

        # Set main layout
        layout = QVBoxLayout()
        layout.addWidget(self.view1)
        layout.addWidget(self.view2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


model = Model()
controller = Controller(model)

app = QApplication([])
window = MainWindow(controller)
window.show()
app.exec_()

