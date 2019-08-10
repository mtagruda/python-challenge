import os
import csv
csvpath = os.path.join("..", "Resources", "budget_data.csv")
revenue = []
date = []
rev_change = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        revenue.append(int(row[1]))
        date.append(row[0])
    print("Financial Analysis")
print("---------------------------------------------------------------------")
print("Total Months: ", len(date))
print("Total: $", sum(revenue))
for i in range(1, len(revenue)):
    rev_change.append(revenue[i] - revenue[i-1])   
    avg_rev_change = sum(rev_change)/len(rev_change)
    max_rev_change = max(rev_change)
    min_rev_change = min(rev_change)
    max_rev_change_date = str(date[rev_change.index(max(rev_change))])
    min_rev_change_date = str(date[rev_change.index(min(rev_change))])
print("Average Change: ", round(avg_rev_change))
print("Greatest Increase in Profits:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Profits:", min_rev_change_date,"($", min_rev_change,")")
file = '../Resources/input.txt'
with open(file, 'w') as text:
      print("Financial Analysis")
print("---------------------------------------------------------------------")
print("Total Months: ", len(date))
print("Total: $", sum(revenue))
for i in range(1, len(revenue)):
    rev_change.append(revenue[i] - revenue[i-1])   
    avg_rev_change = sum(rev_change)/len(rev_change)
    max_rev_change = max(rev_change)
    min_rev_change = min(rev_change)
    max_rev_change_date = str(date[rev_change.index(max(rev_change))])
    min_rev_change_date = str(date[rev_change.index(min(rev_change))])
print("Average Change: ", round(avg_rev_change))
print("Greatest Increase in Profits:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Profits:", min_rev_change_date,"($", min_rev_change,")")



