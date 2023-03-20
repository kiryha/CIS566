"""
This project involves implementing a hotel room bidding system that utilizes the chain of responsibility (COR) design pattern.
The system allows customers to bid on available hotel rooms, and the COR pattern is used to handle the bid requests.
"""

from PySide2 import QtWidgets, QtGui
from ui import main_window


class HotelRoom:
    def __init__(self, room_type, price_range, rooms_available):
        self.room_type = room_type
        self.price_range = price_range
        self.rooms_available = rooms_available

    def __str__(self):
        return f"{self.room_type} - Price Range: {self.price_range}, Rooms Available: {self.rooms_available}"


class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_bid(self, bid_amount, room_type):
        if self.can_accept_bid(bid_amount, room_type):
            return True
        elif self.successor is not None:
            return self.successor.handle_bid(bid_amount, room_type)
        else:
            return False

    def can_accept_bid(self, bid_amount, room_type):
        pass


class StandardRoomHandler(Handler):
    rooms_available_standard = 45

    def can_accept_bid(self, bid_amount, room_type):
        if room_type == "Standard":
            if 80 <= bid_amount <= 150 and self.rooms_available_standard > 0:
                self.rooms_available_standard -= 1
                return True
        return False


class DeluxeRoomHandler(Handler):
    rooms_available_deluxe = 15

    def can_accept_bid(self, bid_amount, room_type):
        if room_type == "Deluxe":
            if 150 <= bid_amount <= 280 and self.rooms_available_deluxe > 0:
                self.rooms_available_deluxe -= 1
                return True
        return False


class SuiteRoomHandler(Handler):
    rooms_available_suite = 10

    def can_accept_bid(self, bid_amount, room_type):
        if room_type == "Suite":
            if bid_amount >= 280 and self.rooms_available_suite > 0:
                self.rooms_available_suite -= 1
                return True
        return False


class HotelRoomUI(QtWidgets.QMainWindow, main_window.Ui_HotelRoom):
    def __init__(self):
        super(HotelRoomUI, self).__init__()
        self.setupUi(self)
        self.comRoomType.addItems(['Standard', 'Deluxe', 'Suite'])

        # Initialize hotel rooms
        self.standard_room = HotelRoom("Standard", "$80 - $150", 45)
        self.deluxe_room = HotelRoom("Deluxe", "$150 - $280", 15)
        self.suite_room = HotelRoom("Suite", "$280 and above", 10)

        # Initialize handlers
        self.standard_handler = StandardRoomHandler()
        self.deluxe_handler = DeluxeRoomHandler()
        self.suite_handler = SuiteRoomHandler()

        # Chain the handlers together
        self.standard_handler.successor = self.deluxe_handler
        self.deluxe_handler.successor = self.suite_handler

        # Handle bid requests
        # self.handle_requests()
        # self.check_availability()

        # UI
        self.btnBid.clicked.connect(self.process_bid)

    def handle_requests(self):

        bid_requests = [
            {"room_type": "Standard", "bid_amount": 120},
            {"room_type": "Deluxe", "bid_amount": 180},
            {"room_type": "Suite", "bid_amount": 300},
            {"room_type": "Standard", "bid_amount": 90},
            {"room_type": "Deluxe", "bid_amount": 250},
            {"room_type": "Suite", "bid_amount": 400},
        ]

        # Handle the bid requests
        for request in bid_requests:
            if not self.standard_handler.handle_bid(request["bid_amount"], request["room_type"]):
                print(f"No handler found for {request['room_type']} room with bid amount of {request['bid_amount']}")
            else:
                print(
                    f"Bid request for {request['room_type']} room with bid amount of {request['bid_amount']} accepted.")

    def check_availability(self):
        if self.standard_room.rooms_available == 0 and \
           self.deluxe_room.rooms_available == 0 and \
           self.suite_room.rooms_available == 0:
            print("All rooms are booked out.")
        else:
            print("\nCurrent Available Rooms:")
            print(self.standard_room)
            print(self.deluxe_room)
            print(self.suite_room)

    def process_bid(self):

        self.txtResults.clear()
        customer_bid = int(self.linBidAmount.text())
        customer_room_type = self.comRoomType.currentText()

        if self.standard_handler.handle_bid(customer_bid, customer_room_type):
            message = f"Congratulations! Your bid of {customer_bid} for a {customer_room_type} room has been accepted."
        else:
            message = f"Sorry, your bid of {customer_bid} for a {customer_room_type} room has been rejected. " \
                      f"Please try again with a different bid amount."

        self.txtResults.append(message)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    hotel_room = HotelRoomUI()
    hotel_room.show()
    app.exec_()

