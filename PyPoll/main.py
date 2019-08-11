import os
import csv
csvpath = os.path.join("..", "Resources", "election_data.csv")
voterid = 0
candidate = []
count = []
maxvotes = []
percentvotes = []
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
            maxvote.append(newcandidate)
        
        voterid = voterid + 1
maxvotes = max(count)
percentvote = (maxvotes / voterid) * 100            
print("Election Results")
print("---------------------------------------------------------------------")
print("Total Votes: ", (voterid))
print("---------------------------------------------------------------------")
for x in range(len(candidate)):
        print(candidate[x])
        print()
print("---------------------------------------------------------------------")
print("Winner: ", (candidate[x-3]) )
print("---------------------------------------------------------------------")
file = '../Resources/input.txt'
with open("output.txt", 'w') as textfile:
    textfile.write(f"Election Results \n --------------------------------------------------------------------- \n Total Votes: {(voterid)} \n --------------------------------------------------------------------- \n {(candidate[x-3])} \n {(candidate[x-2])}  \n {(candidate[x-1])}  \n {(candidate[x])} \n --------------------------------------------------------------------- \n Winner: {(candidate[x-3])} \n ---------------------------------------------------------------------")
