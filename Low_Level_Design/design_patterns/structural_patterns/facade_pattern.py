class VerifiedUsers:
    def __init__(self):
        self.users = {"nick", "steeve", "tony"}
    
    def verify_user(self, user):
        if user in self.users:
            return True
        return False

class SeatAvailability:
    def __init__(self):
        self.types = { "seater": 2, "sleeper": 2 }
    
    def check_availability(self, type):
        if type in self.types:
            return self.types.get(type, 0) != 0
        return "Invalid Seat Type"

class Notification:
    def send_notification(self, user, _type, status):
        return f"Booking Details:\n User: {user}\n Type: {_type}\n Status: {status}\n"

class FacadeBooking:
    def __init__(self):
        self.verified_users = VerifiedUsers()
        self.seat_availability = SeatAvailability()
        self.notification = Notification()
    
    def book(self, user, _type):
        user, _type = user.lower(), _type.lower()
        if self.verified_users.verify_user(user):
            if self.seat_availability.check_availability(_type):
                self.seat_availability.types[_type] -= 1
                return self.notification.send_notification(user, _type, "Success")
            return self.notification.send_notification(user, _type, "Fail")
        return "Invalid User\n"

#client
ticket = FacadeBooking()
print(ticket.book("nick", "sleeper"))
print(ticket.book("Steeve", "sleeper"))
print(ticket.book("thor", "sleeper"))
