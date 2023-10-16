# Importing modules
import os
import csv
import statistics
from statistics import mean


#
budget_csv = os.path.join("Resources", "budget_data.csv")

# Variables
Date = []
Total = 0
#Avg_Change = "A number"/Total_Months
Great_inc_profit = []
Great_dec_profit = []
Total_month = {}



# with open as csvfile:
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row first (skip this step if there is no header)
    next(csvreader)

    for row in csvreader:
        
        # Add date
        Date = str(row[0])

        # Add profit and losses and sum the column
        Total += int(row[1])

        # Split date into month and day
        split_date = row[0].split("-")
        months = split_date[0]
        day = int(split_date[1])

        # Calculate total entries
        if months in Total_month:
            Total_month[months] += 1
        else: 
            Total_month[months] = 1
    Total_month = sum(Total_month.values())
    print(Total_month)

    print(Total)


    

    
       
       

# Calculations




# PL calc
# greatest increase and greatest decrease

# Writing to txt
#output_path = os.path.join("Analysis", "PyBank_Analysis.txt")
#output = "Financial Analysis\n"
#output += "------------------------\n"
#output += f"Total Months: {Total_month}\n"
#output += f"Total: {Total}\n"
#output += f"Average Change: ${round(Avg_Change, 2)}\n"
#output += f"Greatest Increase in Profits: Month (Profit)\n"
#output += f"Greatest Decrease in Profits: Month (Loss)\n"

#with open(output_path, 'w') as output_file:
    #output_file.write(output)
   

#Final Output to Terminal
#print("Financial Analysis")
#print("------------------------")
#print(f"Total Months: {Total_month}")
#print(f"Total: {Total})
#print(f"Average Change: ${round(Avg_Change, 2)}")
#print(f"Greatest Increase in Profits: Month (Profit)")
#print(f"Greatest Decrease in Profits: Month (Loss)")
