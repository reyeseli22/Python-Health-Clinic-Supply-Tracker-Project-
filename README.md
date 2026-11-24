# Python Health Clinic Supply Tracker QAR
## Questions 
- Which supplies run low most often?
- What number constitutes "low stock" ?
- What does supply consumption rate look like on a average day, a busy day and a slow day?
- What fields are required?
A: COMMAND,item name,quantity,category
- What Data Types are present
- How is the Data quality?
> How old is the data? 

> is the data ordered?

> is the data correct/valid? 

> are there any missing fields? duplicates?

> Will we need to cast any data types?
- What calculations will need to be performed?
- Who will be accesing this data? How should it be presented (repr or str)
 ## Assumptions 
- We are working with a large health clinic and need to treat the data accordingly
- No value = Missing field
- ADD = 4 fields(cmd, item, qty, cat)
- Remove = 3 fields(no cat)
- Search = 2 fields(cmd, item)
- search wont change stock, only looks up an item >> what will we report when seached?
- Each row = one transaction (ADD,RMV,SRCH)
- Current stock = running total >> if qty <= running total print low stock
- Priya's team will be accesing this data

> They are not programmers
- We will need to loop the data to find...
> Number of types of supplies and their totals each

>The min, med, max and mean
- We will need to use int() on quantity
# For Now:
- Low count is lower than 15

## Risks
- Missing values would skew our results
- duplicate rows may give us an innacurate measure of usage
- ^ Can mess up the min, med, max and mean
- if an int is required in a field but a str is provided it may break the code 
- remove on that is more than whats in stock will result in negatives
- Typos may result in skipped lines and or innacurate results
- Because there is no category on remove or search we will have to match its cat with an earlier add to validate

## Plan 
1. Read the file into a list of lines
2. Validate each line 
- right number of fields
- qty is an int < 0 (no negatives)
3. Update stock for valid lines
- ADD: += qty
- Remove: -= qty
4. Report all Bad lines (don't count)
5. Find low stock
- qty <= 15 
- print("low stock", qty, cat)
## What will hold the data?
# Because we will need to look up an item by name we will use a dict {}
- stock = {} >> item name, current count
