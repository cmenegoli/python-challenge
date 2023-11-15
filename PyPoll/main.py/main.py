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

with open(input_file) as votes_rollup:

    reader = csv.reader(votes_rollup)

#Header

header = next(reader)

#Row by row

for row in header:

#Accumulate votes

    total_votes += 1

# Initialize candidate names and votes received by them




