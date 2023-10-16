# Importing modules
import os
import csv
import statistics
from statistics import mean


#
budget_csv = os.path.join("Resources", "budget_data.csv")

# Variables
date = []
total = 0
average_change = 0
great_inc_profit = []
great_dec_profit = []
total_month = {}



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
    total_month = sum(total_month.values())
    print(total_month)

    print(total)
    #Create a dictionary aligning the month and the values from row1 to then do the calcs for avg change


    

    
       
       

# Calculations
#Avg_Change = (Feb-Jan, + Mar-Feb + etc...)/total_months



# PL calc
# greatest increase and greatest decrease

# Writing to txt
#output_path = os.path.join("Analysis", "PyBank_Analysis.txt")
#output = "Financial Analysis\n"
#output += "------------------------\n"
#output += f"Total Months: {total_month}\n"
#output += f"Total: {total}\n"
#output += f"Average Change: ${round(Avg_Change, 2)}\n"
#output += f"Greatest Increase in Profits: Month (Profit)\n"
#output += f"Greatest Decrease in Profits: Month (Loss)\n"

#with open(output_path, 'w') as output_file:
    #output_file.write(output)
   

#Final Output to Terminal
#print("Financial Analysis")
#print("------------------------")
#print(f"Total Months: {total_month}")
#print(f"Total: {total})
#print(f"Average Change: ${round(Avg_Change, 2)}")
#print(f"Greatest Increase in Profits: Month (Profit)")
#print(f"Greatest Decrease in Profits: Month (Loss)")
