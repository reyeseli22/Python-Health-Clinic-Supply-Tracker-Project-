




import json
from wsgiref import validate
DATA = "/Users/Marcy_Student/Documents/Marcy/Python-Health-Clinic-Supply-Tracker-Project-/data/healthcare_transactions.txt"


# print(len(lines)) << Checking line count 
# Lines in data = 430
LOW_STOCK_LIMIT = 15

class Healthcare_Supply:
    """
    One supply item in the clinic's inventory
    Tracks the item's name, current quantity and category
    low_stock = when an items quantity dips to less than 15
    """
    
    def __init__(self, name, qty, cat):
        self.name = name
        self.qty = qty
        self.cat = cat


    def is_low_stock(self):
        """Returns True if an item is below LOW_STOCK_LIMIT"""
        if self.qty < LOW_STOCK_LIMIT:
            return True
        else:
            if self.qty >= LOW_STOCK_LIMIT:
                return False 

med_gloves = Healthcare_Supply("Nitrile Exam Gloves (M)",48,"PPE")
lrg_gloves = Healthcare_Supply("Nitrile Exam Gloves (L)",15,"PPE")
# Two objects/instances

# print("Before")
# print("Medium Gloves: ", med_gloves.qty, med_gloves.is_low_stock())
# print("Large Gloves: ", lrg_gloves.qty, lrg_gloves.is_low_stock())

# lrg_gloves.qty = 5

# print()
# print("After")
# print("Medium Gloves: ", med_gloves.qty, med_gloves.is_low_stock())
# print("Large Gloves: ", lrg_gloves.qty, lrg_gloves.is_low_stock())
# Testing methods




    # def almost_low_stock(self):
    #     """Validates if an item is near the low stock limit"""
    #     if self.qty < 20:
    #         return True


def read_batch_file(filepath):
    """
    Reads the file, and returns a list of lines
    """
    with open(DATA) as f:
        return f.read().splitlines()

line = read_batch_file(DATA)

# print(len(lines))
# Testing if read_batch_file reads data as expected 


def validate_line(line):
    """Decides whether a line is a valid ADD, REMOVE, or SEARCH."""
    parts = line.split(",")
    command = parts[0]

    if command == "ADD" and len(parts) == 4:
        try:
            quantity = int(parts[2])
        except ValueError:
            return False, "qty is not a number"
        if quantity < 0:
            return False, "qty is negative"
        if not parts[1].strip():
            return False, "item name is blank"
        if not parts[3].strip:
            return False, "category blank"

        
    elif command == "REMOVE" and len(parts) == 3:
        if not parts[1].strip():
            return False, "item name is blank"
        try:
            quantity = int(parts[2])
        except ValueError:
            return False, "qty is not a number"
        if quantity < 0:
            return False, "qty is negative"
    elif command == "SEARCH" and len(parts) == 2:
        if not parts[1].strip():
            return False, "item name is blank"
    else:
        return False, "unknown command or wrong field count"
    return True, "Valid Input"

print(validate_line("ADD,Hand Sanitizer 8oz,19,PPE"))
print(validate_line("ADD,Compression Stockings,22,Wound Care"))
print(validate_line("SEARCH,Surgical Face Masks"))
print(validate_line("SEARCH,Urine Test Strips"))
print(validate_line("REMOVE,Acetaminophen 500mg,3"))
print(validate_line("REMOVE,Face Shields,5"))

"""TODO: write your own docstring. What makes an ADD, REMOVE, or
SEARCH line valid? What do you return for a valid line, and what for
    an invalid one?"""
    # TODO: implement. One choice worth making on purpose: a quantity can
    # be present but not a number ("five"). Wrap int(quantity) in a
    # try/except ValueError. That asks Python "did this work?" instead
    # of trying to predict every way it could fail.
pass


def process_transactions(lines):
    """TODO: write your own docstring."""
    # TODO: implement. Loop over the lines, apply each valid one to your
    # collection of items, and print a specific message for each line
    # you skip. Return the collection at the end. The full inventory
    # printout is print_summary's job, not this function's.
    pass


def find_item(items, name):
    """TODO: write your own docstring."""
    # TODO: implement
    pass


def export_to_json(items, filepath="inventory.json"):
    """TODO: write your own docstring. json.dump can't write your objects
    directly, so turn each one into a dict first."""
    # TODO: implement
    pass


def print_summary(items):
    """TODO: write your own docstring."""
    # TODO: implement. This one only prints, so it doesn't need to return
    # anything.
    pass


# TODO: point this at the data file for the scenario you chose.
lines = read_batch_file("data/____________.txt")
items = process_transactions(lines)
print_summary(items)
export_to_json(items)
