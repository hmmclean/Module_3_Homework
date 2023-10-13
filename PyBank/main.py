# Importing modules
import os
import csv
import statistics
from statistics import mean


#
budget_csv = os.path.join("Resources", "budget_data.csv")

# List to store data
Date = []
P = "profit"
L = "losses"
PL = P + L 
Total = PL
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

        # Add profit and losses
        Total = int(row[1])

        # Split date into month and day
        split_date = row[0].split("-")
        months = split_date[0]
        day = int(split_date[1])
        if months in Total_month:
            Total_month[months] += 1
        else: 
            Total_month[months] = 1
    Total_month = sum(Total_month.values())
    print(Total_month)
       
       

# Calculations




# PL calc
# greatest increase and greatest decrease

# Writing to txt
with open('PyBank.txt', 'w', encoding='utf-8') as f:
    #f.write(PyBank)
    f.write("Financial Analysis\n")
    f.write("------------------------\n")
    #f.write(f"Total Months: {Total_Months}\n")
    #f.write(f"Average Change: ${round(Avg_Change, 2)}\n")
    #f.write(f"Greatest Increase in Profits: Month (Profit)\n")
    #f.write(f"Greatest Decrease in Profits: Month (Loss)\n")

#Final Output
print("Financial Analysis")
print("------------------------")
#print(f"Total Months: {Total_Months}")
#print(f"Average Change: ${round(Avg_Change, 2)}")
#print(f"Greatest Increase in Profits: Month (Profit)")
#print(f"Greatest Decrease in Profits: Month (Loss)")
