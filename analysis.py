import json
from wsgiref import validate
DATA = "/Users/Marcy_Student/Documents/Marcy/Python-Health-Clinic-Supply-Tracker-Project-/data/healthcare_transactions.txt"


# print(len(lines)) << Checking line count 
# Lines in data = 430
LOW_STOCK_LIMITS = {"PPE":25, "Wound Care":20, "Medication":20, "Equipment": 15}
DEFAULT_LIMIT = 15

inventory ={"PPE":{}, "Wound Care":{}, "Medication": {}, "Equipment":{}}
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
        if self.qty < LOW_STOCK_LIMITS.get(self.cat, DEFAULT_LIMIT):
            return True
        else:
            if self.qty >= LOW_STOCK_LIMITS:
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
    """Decides whether a line is a valid ADD, REMOVE, or SEARCH.
    Valid lines:
    - ADD: 4 fields (command, item, qty, category)
    - REMOVE: 3 fields (command, item, qty)
    - SEARCH: 2 fields (command, item)

    Returns (True, "Valid Input") for a valid line, or
    (False, reason) why it was rejected.
    """
    parts = line.split(",")
    command = parts[0].upper()
    #####ADD######
    if command == "ADD" and len(parts) == 4:
        try:
            quantity = int(parts[2])
        except ValueError:
            return False, "qty is not a number"
        if quantity < 0:
            return False, "qty is negative"
        if not parts[1].strip():
            return False, "item name is blank"
        if not parts[3].strip():
            return False, "category blank"
    ######REMOVE#### 
    elif command == "REMOVE" and len(parts) == 3:
        if not parts[1].strip():
            return False, "item name is blank"
        try:
            quantity = int(parts[2])
        except ValueError:
            return False, "qty is not a number"
        if quantity < 0:
            return False, "qty is negative"
    #######SEARCH######
    elif command == "SEARCH" and len(parts) == 2:
        if not parts[1].strip():
            return False, "item name is blank"
    else:
        return False, "unknown command or wrong field count"
    return True, "Valid Input"

print(validate_line("ADD,Elastic Bandages,7,Wound Care,extra,fields")) #Edge-case 1 found by hand line 358: contains 6 fields
print(validate_line("SEARCH,")) # Edge-case 2 found by hand line 383 , Only Command in SEARCH all other fields blank
print(validate_line("ADD,Saline Solution 500mL,five,Medication")) # Edge-Case 3 found by hand line 147: "five" in qty instead of 5, would cause value error



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