import os
import csv
csvpath = os.path.join("..", "Resources", "election_data.csv")
def print_percentage(candidate_data):
    cname = str(candidate_data[0])
    vwin = int(candidate_data[1])
    vloss = int(candidate_data[2])
total_votes = (vwin + vloss)
vwin_percent = (vwin / total_votes)*100
top_percent = 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        if 
            print("Election Results")
print("---------------------------------------------------------------------")
print("Total Votes: ", sum(voterid))
print("---------------------------------------------------------------------")
print("List of top 4 candidates", max(candidate), )
print("---------------------------------------------------------------------")
print("Winner: ", max(candidate))
print("---------------------------------------------------------------------")
