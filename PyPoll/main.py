import os
import csv
csvpath = os.path.join("..", "Resources", "election_data.csv")
voterid = 0
candidate = []
count = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        newcandidate = row[2]
        if not newcandidate in candidate:
            candidate.append(newcandidate)
            count.append(1)
        else:
            thisindex=candidate.index(newcandidate)
            count[thisindex]= candidate.index(newcandidate)
        
        voterid = voterid + 1
maxvotes = max(count)            
print("Election Results")
print("---------------------------------------------------------------------")
print("Total Votes: ", (voterid))
print("---------------------------------------------------------------------")
print("List of top 4 candidates" )
for x in range(len(candidate)):
        print(candidate[x], count[x])
print("---------------------------------------------------------------------")
print("Winner: ")
print("---------------------------------------------------------------------")
