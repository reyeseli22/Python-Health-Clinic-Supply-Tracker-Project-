import json
from wsgiref import validate
DATA = "/Users/Marcy_Student/Documents/Marcy/Python-Health-Clinic-Supply-Tracker-Project-/data/healthcare_transactions.txt"


# print(len(lines)) << Checking line count 
# Lines in data = 430
LOW_STOCK_LIMITS = {"PPE":25, "Wound Care":20, "Medication":20, "Equipment": 15}
DEFAULT_LIMIT = 15

inventory = {"PPE":{}, "Wound Care":{}, "Medication": {}, "Equipment":{}}
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
        """Returns True if an item is below a particular category's limit"""
        if self.qty < LOW_STOCK_LIMITS.get(self.cat, DEFAULT_LIMIT):
            return True, "Low Stock"
        else: 
            return False, "In Stock"

    def add(self, amount):
        """increase a particular item's qty by amount given"""
        self.qty += amount


    def remove(self, amount):
        """Decrease qty by amount given
        Returns: True, reason on a valid add
        Returns False, reason on invalid add
        if amount is more than in stock, qty will remain unchanged"""
        if amount > self.qty:
            return False, "removed more than in stock"
        self.qty -= amount
        return True, "Removed"


med_gloves = Healthcare_Supply("Nitrile Exam Gloves (M)",48,"PPE")
lrg_gloves = Healthcare_Supply("Nitrile Exam Gloves (L)",15,"PPE")
ibuprofen_pills = Healthcare_Supply("Ibuprofen 200mg", 14, "Medication")
# Two objects/instances

# print("Before")
# print("Medium Gloves: ", med_gloves.qty, med_gloves.is_low_stock())
# print("Large Gloves: ", lrg_gloves.qty, lrg_gloves.is_low_stock())
# print("Ibuprofen",ibuprofen_pills.qty, ibuprofen_pills.is_low_stock())
# lrg_gloves.qty = 26
# ibuprofen_pills.qty = 21
#lrg_gloves.add(10)
# print(lrg_gloves.remove(100))   # (False, 'removed `qmore than in stock')
# print(lrg_gloves.remove(6))     # (True, 'Removed')
# print()
# print("After")
# print("Medium Gloves: ", med_gloves.qty, med_gloves.is_low_stock())
# print("Large Gloves: ", lrg_gloves.qty, lrg_gloves.is_low_stock())
# print("Ibuprofen",ibuprofen_pills.qty, ibuprofen_pills.is_low_stock())
# print()
# print("after add")
# lrg_gloves.add(10)
# print(lrg_gloves.qty)            
# print(lrg_gloves.remove(100))    
# print(lrg_gloves.qty)             
# print(lrg_gloves.remove(6))       
# print(lrg_gloves.qty)             
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
    if not line.strip():
        return False, "Blank Line"
    if parts[0] != parts[0].strip().upper(): # catches non-capitalized commands and commands with spaces around them
        print("Fixed lowercase command: ", repr(line)) 
    
    command = parts[0].upper() #  lowercase commands are capitalized
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
        if parts[3].strip() not in LOW_STOCK_LIMITS:
            return False, "Unknown Category"
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

# print(validate_line("ADD,Elastic Bandages,7,Wound Care,extra,fields")) #Edge-case 1 found by hand line 358: contains 6 fields
# print(validate_line("SEARCH,")) # Edge-case 2 found by hand line 383 , Only Command in SEARCH all other fields blank
# print(validate_line("ADD,Saline Solution 500mL,five,Medication")) # Edge-Case 3 found by hand line 147: "five" in qty instead of 5, would cause value error

# for number, line in enumerate(line, start=1):
#     is_valid, reason = validate_line(line)
#     if not is_valid:
#         print(number, repr(line), reason).  <<< Test Scan Loop: lists every rejected line and its line number 


def process_transactions(lines):
    """Loops over each line
    Applies each valid line to inventory with relevant command
    Skips invalid lines and counts total skipped lines"""
    skipped = 0
    inventory = {"PPE":{}, "Wound Care":{}, "Medication": {}, "Equipment":{}}
    for line in lines:
        is_valid, reason = validate_line(line)
        if not is_valid:
            skipped += 1
            print(f"SKIPPED: {line} | {reason}")
            continue

        parts = line.split(",")
        if parts[1] != parts[1].strip() or (len(parts) == 4 and parts[3] != parts[3].strip()):
            print(f"Whitespace removed {line!r}") # catches lines with whitespace and fixes them as to not mess up counts quietly
        command = parts[0].strip().upper()
        name = parts[1].strip()
        ## every valid command has atleast a command and name split by ","###
        if command == "ADD":
            qty = int(parts[2])
            cat = parts[3].strip()
            if cat not in inventory: 
                skipped +=1 
                print(f"SKIPPED: {line!r} | Unknown category")
                continue
            if name in inventory[cat]:
                inventory[cat][name].add(qty)
            else:
                inventory[cat][name] = Healthcare_Supply(name, qty, cat)
        elif command == "REMOVE":
            qty = int(parts[2])
            item = find_item(inventory, name)
            if item is None:
                skipped += 1
                print(f"SKIPPED: {line!r} | Item Not Found")
                continue
            ok, reason = item.remove(qty)
            if not ok:
                skipped += 1 
                print(f"SKIPPED: {line!r} | {reason}")
        elif command == "SEARCH":
            item = find_item(inventory, name)
            if item is None:
                print(f"ITEM NOT FOUND : {name}")
            else: 
                print(f"ITEM FOUND: {item.name} | {item.cat} | {item.qty}")
    print("Total lines: ", len(lines), "| SKIPPED: ", skipped)
    return inventory
    # TODO: implement. Loop over the lines, apply each valid one to your
    # collection of items, and print a specific message for each line
    # you skip. Return the collection at the end. The full inventory
    # printout is print_summary's job, not this function's.



def find_item(items, name):
    """TODO: Returns the item. None if not found """
    for category in inventory.values():
        if name in category:
            return category[name]
    return None




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