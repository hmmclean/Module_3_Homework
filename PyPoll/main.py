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

# Calculate candidate vote percentage
ccs_percent = format((total_ccs_votes/total_num_votes), ".0%")
dg_percent = format((total_dg_votes/total_num_votes), ".0%")
rad_percent = format((total_rad_votes/total_num_votes), ".0%")


# Populate dictionary to associate winner name and total votes
vote_candidate = dict([(total_ccs_votes, candidates[0]), (total_dg_votes, candidates[1]), (total_rad_votes, candidates[2])])
max_votes = max(total_ccs_votes,total_dg_votes,total_rad_votes)


# Writing to txt
output_path = os.path.join("Analysis", "PyPoll_Analysis.txt")
output = "Election Results\n"
output += "--------------------\n"
output += f"Total Votes: {total_num_votes}\n"
output += "--------------------\n"
output += f"{candidates[0]}: {ccs_percent} ({total_ccs_votes})\n"
output += f"{candidates[1]}: {dg_percent} ({total_dg_votes})\n"
output += f"{candidates[2]}: {rad_percent} ({total_rad_votes})\n"
output += "--------------------\n"
output += f"Winner: {vote_candidate[max_votes]}\n"
output += "--------------------\n"

with open(output_path, 'w') as output_file:
    output_file.write(output)

print(output)
   

# Final Output to Terminal
print("Election Results")
print("--------------------")
print("Total Votes: ", total_num_votes)
print("--------------------")
print(f"{candidates[0]}: {ccs_percent} ({total_ccs_votes})")
print(f"{candidates[1]}: {dg_percent} ({total_dg_votes})")
print(f"{candidates[2]}: {rad_percent} ({total_rad_votes})")
print("--------------------")
print("Winner: ", vote_candidate[max_votes])
print("--------------------")