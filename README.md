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
- Valid Input = Line with 4 fields 
- Each row = one supply count for one day
- Priya's team will be accesing this data

> They are not programmers
- We will need to loop the data to find...
> Number of types of supplies and their totals each

>The min, med, max and mean
# For Now:
- Low count is lower than 15

## Risks
- Missing values would skew our results
- duplicate rows may give us an innacurate measure of usage
- ^ Can mess up the min, med, max and mean
- if an int is required in a field but a str is provided it may break the code 
- 