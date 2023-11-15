import os
import csv

#set variables
totalmonths = 0
totalPL = 0
date = []
profitloss = []
greatestincrease = 0
greatestdecrease = 0

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# open file and read, store contents as text
with open(csvpath) as csvfile:

    #store reference to file and set comma to indicate new row
    budget_data = csv.reader(csvfile, delimiter=',')

    # skip the header row
    budget_header = next(budget_data)

    #Begin output
    print("Financial Analysis")
    print("---------------------------")

     # as reading data calculate
    for row in budget_data:
        # the total number of months included in the data set
        total_month += 1
        # change in profit and record it in next column
        change_profit = int(row[1])-profit
        profit = int(row[1])
        # total profit for the data set
        total_profit += profit
        # total change in profit 
        total_change += change_profit
        # identify maximum increase in profit
        if change_profit > max_change:
            max_change = change_profit
            max_month = str(row[0])
        # identify the maximum decrease in profit
        if change_profit < min_change:
            min_change = change_profit
            min_month = str(row[0])
       
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

