class LibraryItem:

    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._location = 'ON-SHELF'

    def get_location(self):
        return self._location
    
class Book(LibraryItem):
    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author
        self._check_out_length = 21

    def get_author(self):
        return self._author 

    def get_check_out_length(self):
        return self._check_out_length

class Movie(LibraryItem):
    
    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director
        self._check_out_length = 7
    
    def get_director(self):
        return self._director 

    def get_check_out_length(self):
        return self._check_out_length

class Album(LibraryItem):

    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist
        self._check_out_length = 14

    def get_artist(self):
        return self._artist

    def get_check_out_length(self):
        return self._check_out_length
    

class Patron:

    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_fine_amount(self):
        return self._fine_amount
    
    def get_checked_out_items(self):
        return self._checked_out_items
    
    def add_library_item(self):
        pass

    def remove_library_item(self):
        pass

    def amend_fine(self):
        pass


class Library:

    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0 #num of days since open


    def add_library_item(self, library_item_object):
        pass
        #adds library_item_object to holdings

    def add_patron(self, patron_object):
        pass
        # add patron_object to members

    def lookup_library_item_from_id(self, library_item_id):
        pass
        # returns library item object that corresponds to the library_item_id or None

    def lookup_patron_from_id(self, patron_id):
        pass
        # returns patron object given the patron ID or None

    def checkout_library_item(self, patron_id, library_item_id):
        pass
        # takes as parameters a patron ID and a library item ID, in that order
# if the specified Patron is not in the Library's members, return "patron not found"
# if the specified LibraryItem is not in the Library's holdings, return "item not found"
# if the specified LibraryItem is already checked out, return "item already checked out"
# if the specified LibraryItem is on hold by another Patron, return "item on hold by other patron"
# otherwise update the LibraryItem's checked_out_by, date_checked_out and location
# if the LibraryItem was on hold for this Patron, update requested_by
# update the Patron's checked_out_items
# return "check out successful"

    def return_library_item(self, patron_id, library_item_id):
        pass
        # not sure if it needs patron_id so its a placeholder for now
#         if the specified LibraryItem is not in the Library's holdings, return "item not found"
# if the LibraryItem is not checked out, return "item already in library"
# update the Patron's checked_out_items
# update the LibraryItem's location depending on whether another Patron has requested it (if so, it should go on the hold shelf)
# update the LibraryItem's checked_out_by
# return "return successful"

    def request_library(self, patron_id, library_item_id):
        pass
#     takes as parameters a patron ID and a library item ID, in that order
# if the specified Patron is not in the Library's members, return "patron not found"
# if the specified LibraryItem is not in the Library's holdings, return "item not found"
# if the specified LibraryItem is already requested, return "item already on hold"
# update the LibraryItem's requested_by
# if the LibraryItem is on the shelf, update its location to on hold
# return "request successful"

    def pay_fine(self, patron_id, paid_amount):
        pass
# takes as parameters a Patron ID and the amount (in dollars) being paid (in that order)
# if the specified Patron is not in the Library's members, return "patron not found"
# use amend_fine to update the Patron's fine; return "payment successful"

    def increment_current_date(self):
        pass
# takes no parameters
# increment current date
# increase each Patron's fines by 10 cents for each overdue LibraryItem they have checked out (by calling amend_fine)
# Note - a LibraryItem can be on request without its location being the hold shelf (if another Patron has it checked out);



b1 = Book("345", "Phantom Tollbooth", "Juster")
# a1 = Album("456", "...And His Orchestra", "The Fastbacks")
# m1 = Movie("567", "Laputa", "Miyazaki")

print(b1.get_check_out_length())

p1 = Patron("abc", "Felicity")
p2 = Patron("bcd", "Waldo")