# Importing modules
import os
import csv

#csv location variable
election_csv = os.path.join("Resources", "election_data.csv")

# Variables
total_num_votes = 0
candidates = []
total_ccs_votes = 0
total_dg_votes = 0
total_rad_votes = 0

# Read csv file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    next(csvreader)

    for row in csvreader:
        # Add voter ID
        votes = str(row[0])

        # Add county
        county = str(row[1])

        # Add candidate
        candidate = str(row[2])

        # Total number of votes cast
        total_num_votes += 1

        # Store candidates names
        if candidate not in candidates:
            candidates.append(candidate)

        # Calculate candidate total number of votes
        if candidate == "Charles Casper Stockham":
            total_ccs_votes += 1
            
        elif candidate == "Diana DeGette":
            total_dg_votes += 1
        
        else: 
            candidate == "Raymon Anthony Doane"
            total_rad_votes += 1

# Calculate candidate percentage
ccs_percent = total_ccs_votes/total_num_votes
dg_percent = total_dg_votes/total_num_votes
rad_percent = total_rad_votes/total_num_votes

# Winner
winner = max(ccs_percent,dg_percent,rad_percent)

print(total_ccs_votes)
print(total_dg_votes)
print(total_rad_votes)

print(format(ccs_percent, ".0%"))
print(format(dg_percent, ".0%"))
print(format(rad_percent, ".0%"))

print(winner)



# Writing to txt
#with open('PyPoll.txt', 'w', encoding='utf-8') as f:
    #f.write(PyPoll)
    #f.write("Election Results\n")
    #f.write("--------------------\n")
    #f.write(f"Total Votes: total_num_votes\n")
    #f.write("--------------------\n")
    #f.write(f"List of candidates\n")
    #f.write("--------------------\n")
    #f.write(f"Winner: \n")
    #f.write("--------------------\n")



# Final Output to Terminal
print("Election Results")
print("--------------------")
print("Total Votes: ", total_num_votes)
print("--------------------")
print("List of candidates: ", candidates)
print("--------------------")
print("Winner: ")
print("--------------------")