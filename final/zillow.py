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


# Views
class View1:
    @staticmethod
    def get_house_info():
        price = int(input("Enter price: "))
        address = input("Enter address: ")
        city = input("Enter city: ")
        zip_code = input("Enter zip code: ")
        year_built = int(input("Enter year built: "))
        property_type = input("Enter property type (single, condo, townhome): ")
        bedrooms = int(input("Enter number of bedrooms: "))

        return House(price, address, city, zip_code, year_built, property_type, bedrooms)

    @staticmethod
    def display_success():
        print("House information added/updated successfully.")


class View2:
    @staticmethod
    def get_search_criteria():
        criteria = {}
        price_range = input("Enter price range (low-high) or leave blank: ")
        if price_range:
            low, high = map(int, price_range.split('-'))
            criteria['price'] = (low, high)
        city = input("Enter city or leave blank: ")
        if city:
            criteria['city'] = city
        zip_code = input("Enter zip code or leave blank: ")
        if zip_code:
            criteria['zip_code'] = zip_code
        year_built = input("Enter year built or leave blank: ")
        if year_built:
            criteria['year_built'] = int(year_built)
        property_type = input("Enter property type (single, condo, townhome) or leave blank: ")
        if property_type:
            criteria['property_type'] = property_type
        bedrooms = input("Enter number of bedrooms or leave blank: ")
        if bedrooms:
            criteria['bedrooms'] = int(bedrooms)

        return criteria

    @staticmethod
    def display_search_results(houses):
        for i, house in enumerate(houses):
            print(f"{i}. {house.address}, {house.city}, {house.zip_code}")


class View3:
    @staticmethod
    def display_house_details(house):
        print(f"Price: ${house.price}")
        print(f"Address: {house.address}")
        print(f"City: {house.city}")
        print(f"Zip: {house.zip_code}")
        print(f"Year built: {house.year_built}")
        print(f"Property type: {house.property_type}")
        print(f"Bedrooms: {house.bedrooms}")


# Controller
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


def zillow_no_gui():
    model = Model()
    controller = Controller(model)

    while True:
        print("\nOptions:")
        print("1. Add/Update house information")
        print("2. Search for houses")
        option = input("Select an option: ")

        if option == "1":
            controller.add_update_house()
        elif option == "2":
            search_results = controller.search_houses()
            if search_results:
                house_index = int(input("Enter the index of the house for more details or -1 to go back: "))
                if house_index != -1:
                    controller.display_house_details(house_index)
        else:
            print("Invalid option, please try again.")

zillow_no_gui()