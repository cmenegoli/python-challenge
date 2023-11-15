import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resources','budget_data.csv')

#set variables
totalmonths = 0
totalPL = 0
date = []
profitloss = []
greatestincrease = 0
greatestdecrease = 0

# open file and read, store contents as text
with open(budget_data) as csvfile:

    #store reference to file and set comma to indicate new row
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip the header row
    header = next(csvreader)
    print(csvreader)

    #Begin output
    print("Financial Analysis")
    print("---------------------------")

    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period      
    # The average of the changes in "Profit/Losses" over the entire period
    for row in csvreader:
        # turn date and pl column into list
        date.append(row[0])
        profitloss.append(float(row[1]))
        
        #counter for number of lines
        totalmonths += 1
        # csv column sum
        totalPL += (int(row[1]))
        #got help from Wei on this equation below
        avgpl = (int(profitloss[0])- int(profitloss[85]))/85

        # zip appended lists together to create tuple to perform max/min features on
        greatestincrease = max(ziplist, key =lambda x:x[1])
        greatestdecrease = min(ziplist,key =lambda x:x[1])
       
    print("Total Months: " + str(totalmonths))    
    print('Total Net Profit/Losses: $' + str(totalPL))
    print("Average Change: $"+ str(avgpl))
    print("Greatest Increase in Profits: " + str(greatestincrease))
    print("Greatest Decrease in Profits: "+ str(greatestdecrease))

    #write above to text file
    PyBank = output_path = os.path.join("analysis", "PyBank.txt")

    with open(PyBank,'w') as file:
        file.write("Financial Analysis\n")
        file.write("---------------------\n")
        file.write(f"Total Months:  {totalmonths}\n")
        file.write(f"Total Net Profit/Losses: $  {totalPL}\n")
        file.write(f"Average Change:  {avgpl}\n")
        file.write(f"Greatest Increase in Profits:   {greatestincrease}\n")
        file.write(f"Greatest Decrease in Profits:   {greatestdecrease}")

