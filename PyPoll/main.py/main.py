# Import modules
import csv
import os

# Load input file
input_file = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidate_choices = [] #candidate names list
candidate_votes = {} #vote counts in dictionary
elected_candidate = ""
elected_count = 0

#Read the input file

with open(input_file, 'r') as votes_rollup:

    reader = csv.reader(votes_rollup)

#Header
header = next(reader)

#Row by row
for row in header:
    total_votes += 1

# Initialize candidate names and votes received by them
    #list of candidates
    candidate_choices.append(row[2]) 
    candidate_votes[row[2]]
    candidate_votes[row[2]] + 1

# Print total votes to terminal
election_results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"\n"
    f"Total Votes: {total_votes}\n"
    f"\n"
    f"-------------------------\n")
print(election_results)

# Now that we have the dictionary built with candidate name and their votes, loop through each candidate
for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    vote_percentage = float(votes) / float(total_votes) * 100

     # Determine who won and their vote count
    if (votes > elected_count):
        elected_count = votes
        elected_candidate = candidate

    # Set election results by candidate to variable results_output
    results_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    print(results_output)

# Print winner to terminal
elected_candidate_summary = (
    f"-------------------------\n"
    f"\n"
    f"Winner: {elected_candidate}\n"
    f"\n"
    f"-------------------------\n")
print(elected_candidate_summary)

# Write to file
output_file = os.path.join("analysis", "election_results.txt")

# Print the results and export the data to election_results.txt
with open(output_file, "w") as txt_file:
    txt_file.write(election_results)
    
    for candidate in candidate_votes:
   
        votes = candidate_votes.get(candidate) 
        vote_percentage = float(votes) / float(total_votes) * 100

    
        if (votes > elected_count):
            elected_count = votes
            elected_candidate = candidate

    
        results_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        txt_file.write(results_output)
        
    txt_file.write(elected_candidate_summary)






   




