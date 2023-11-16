# Import modules
import csv
import os

# Load input file
file_path = r'C:\Users\Carolina\OneDrive\Carolina\python-challenge\PyPoll\election_data.csv'

# Initialize variables
total_votes = 0
candidate_votes = {}

    # Open file and read CSV contents
with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        # Skip the header row
        election_header = next(csvreader)

        # Loop through the rows in the CSV file
        for row in csvreader:
            # Increment total votes
            total_votes += 1

            # Count votes for each candidate
            candidate = row[2]
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1

    # Calculate and print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("-------------------------")

    # Write the results to a text file
output_path = os.path.join("analysis", "Election_Results.txt")
with open(output_path, 'w') as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("-------------------------\n")
        for candidate, votes in candidate_votes.items():
            percentage = (votes / total_votes) * 100
            file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------\n")

# Specify the file path for election data
file_path = r'path/to/your/election_data.csv'




   




