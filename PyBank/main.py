# Importing modules
import os
import csv

# Variable to hold csv location
budget_csv = os.path.join("Resources", "budget_data.csv")

# Variables
date = []
total = 0
total_month = {}
previous = None
average_change = []
great_inc = 0
great_inc_row = None
great_dec = 0
great_dec_row = None

# with open as csvfile:
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row first (skip this step if there is no header)
    next(csvreader)

    for row in csvreader:
        
        # Add date
        date = str(row[0])

        # Add profit and losses and sum the column
        total += int(row[1])

        # Split date into month and day
        split_date = row[0].split("-")
        months = split_date[0]
        day = int(split_date[1])

        # Calculate total entries
        if months in total_month:
            total_month[months] += 1
        else: 
            total_month[months] = 1
    
        # Calculate change in profit and losses
        if row and row[1]:
            current = int(row[1])
            if previous is not None:
                change = current - previous
                average_change.append(change)
                
                # Calculate greatest increase and decrease in profits
                if change > great_inc:
                    great_inc = change
                    great_inc_row = row
                elif change < great_dec:
                    great_dec = change
                    great_dec_row = row        
            previous = current

# Sum total entries   
total_month = sum(total_month.values())

# Calculate average change
if len(average_change) > 0:
    average = sum(average_change) / len(average_change)

# Writing to txt
output_path = os.path.join("Analysis", "PyBank_Analysis.txt")
output = "Financial Analysis\n"
output += "------------------------\n"
output += f"Total Months: {total_month}\n"
output += f"Total: ${total}\n"
output += f"Average Change: ${round(average, 2)}\n"
output += f"Greatest Increase in Profits: {great_inc_row[0]} (${great_inc})\n"
output += f"Greatest Decrease in Profits: {great_dec_row[0]} (${great_dec})\n"

with open(output_path, 'w') as output_file:
    output_file.write(output)
   
# Final Output to Terminal
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${total}")
print(f"Average Change: ${round(average, 2)}")
print(f"Greatest Increase in Profits: {great_inc_row[0]} (${great_inc})")
print(f"Greatest Decrease in Profits: {great_dec_row[0]} (${great_dec})")