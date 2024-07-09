""" 
Single responsibility: one class should not handle more than one responsibility.
"""
# Below, Library1 is handling it's responsibilities and payment responsibity too.
# we have to separate the payment method to achieve single responsibility.

class Library1:
    def __init__(self) -> None:
        self.stock = {"tvd": 2, "originals": 2}

    def borrowBook(self, book_name):
        if self.stock.get(book_name, 0) > 0:
            self.stock[book_name] -= 1
            return f"{book_name} book borrowed"
        return f" *** {book_name} book not in stock *** "
    
    def returnBook(self, book_name):
        if book_name in self.stock:
            self.stock[book_name] += 1
            return f"{book_name} book borrowed"
        return f" *** Invalid Book *** "
    
    # the payment system is not related to this class, so single responsibility has violated
    def payment(self, student_name, due_amount, payment_type):
        if payment_type == "phonepe":
            return f"Student {student_name} paid due amount {due_amount}/- with phonepe"
        if payment_type == "googlepay":
            return f"Student {student_name} paid due amount {due_amount}/- with googlepay"
    
# -----------------------------------------------------------------------------------------------------

class Library2:
    def __init__(self) -> None:
        self.stock = {"tvd": 2, "originals": 2}

    def borrowBook(self, book_name):
        if self.stock.get(book_name, 0) > 0:
            self.stock[book_name] -= 1
            return f"{book_name} book borrowed"
        return f" *** {book_name} book not in stock *** "
    
    def returnBook(self, book_name):
        if book_name in self.stock:
            self.stock[book_name] += 1
            return f"{book_name} book borrowed"
        return f" *** Invalid Book *** "
    
# payment responsibility has separated from the Library2 class to achieve Single Responsibility Model
""" But open-closed principle has violated in below. we'll achieve that in open-closed.py"""
class Payment:
    def payment(self, student_name, due_amount, payment_type):
        if payment_type == "phonepe":
            return f"Student {student_name} paid due amount {due_amount}/- with phonepe"
        if payment_type == "googlepay":
            return f"Student {student_name} paid due amount {due_amount}/- with googlepay"

library1 = Library1()
print(library1.borrowBook("tvd"))
print(library1.returnBook("tvd"))
print(library1.payment("nick", 1000, "phonepe"))

print()

library2 = Library2()
payment = Payment()
print(library1.borrowBook("tvd"))
print(library1.returnBook("tvd"))
print(payment.payment("nick", 1000, "googlepay"))