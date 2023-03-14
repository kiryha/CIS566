"""
This project involves implementing a hotel room bidding system that utilizes the chain of responsibility (COR) design pattern.
The system allows customers to bid on available hotel rooms, and the COR pattern is used to handle the bid requests.
"""


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


# Initialize hotel rooms
standard_room = HotelRoom("Standard", "$80 - $150", 45)
deluxe_room = HotelRoom("Deluxe", "$150 - $280", 15)
suite_room = HotelRoom("Suite", "$280 and above", 10)

# Initialize handlers
standard_handler = StandardRoomHandler()
deluxe_handler = DeluxeRoomHandler()
suite_handler = SuiteRoomHandler()

# Chain the handlers together
standard_handler.successor = deluxe_handler
deluxe_handler.successor = suite_handler


# Simulate bid requests
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
    if not standard_handler.handle_bid(request["bid_amount"], request["room_type"]):
        print(f"No handler found for {request['room_type']} room with bid amount of {request['bid_amount']}")

# Check if any rooms are still available
if standard_room.rooms_available == 0 and deluxe_room.rooms_available == 0 and suite_room.rooms_available == 0:
    print("All rooms are booked out.")
