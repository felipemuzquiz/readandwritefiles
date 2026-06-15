import pandas as pd

# Load the sales CSV file
df = pd.read_csv('sales.csv')

# Create the variable that will store the running totals
c_total = {}

# Create a for loop to sum up all the costs associated with
# each customer
for index, row in df.iterrows():
	
	# Identify the unique Customer IDs in the csv file
	cid = row.iloc[0]
	
	# Calculate total spent per customer
	row_total = row.iloc[3] + row.iloc[4] + row.iloc[5]
	
	# Check to see if this customer has been added to the list
	# being calculated, and if not, create a new entry
	if cid in c_total:
		c_total[cid] += row_total
	else:
		c_total[cid] = row_total
		
# Convert loop data into a Data Frame to be saved as a 
# csv file.
SalesreportFINAL = pd.DataFrame(list(c_total.items()), columns=['Customer ID', 'Total']).round(2)

# Create the SalesreportFINAL csv file
SalesreportFINAL.to_csv('salesreportFINAL.csv', index=False)

# Confirmation that the csv file was created successfully
print("Sales Report FINAL csv file has been created successfully")