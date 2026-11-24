




import json
DATA = "/Users/Marcy_Student/Documents/Marcy/Python-Health-Clinic-Supply-Tracker-Project-/data/healthcare_transactions.txt"
with open(DATA) as f:
    lines = f.read().splitlines()
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
# med_gloves.qty = 15

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
    Read the batch file at `filepath` and return a list of its lines
    (strings), unchanged. Deciding whether a line is usable happens in
    validate_line(), not here. Use this docstring as the model for the
    ones you write below: what the function does, what it takes, and what
    it returns.
    """
    # TODO: implement
    pass


def validate_line(line):
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
