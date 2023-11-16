import os
import csv

#set variables
total_months = 0
total_profit = 0
previous_profit = 0
profit_change_list = []
months_list = []

# Path to collect data from the Resources folder
file_path = r'C:\Users\Carolina\OneDrive\Carolina\python-challenge\PyBank\Resources\budget_data.csv'

# open file and read, store contents as text
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

        # Skip the header row
    header = next(csvreader)

        # Loop through the rows in the CSV file
    for row in csvreader:
            # Increment total months
            total_months += 1

            # Accumulate total profit
            total_profit += int(row[1])

            # Calculate and store profit change
            if total_months > 1:
                profit_change = int(row[1]) - previous_profit
                profit_change_list.append(profit_change)
                months_list.append(row[0])

            # Update previous profit for the next iteration
            previous_profit = int(row[1])

    # Calculate average revenue change
    avg_revenue_change = sum(profit_change_list) / len(profit_change_list)

    # Find the greatest increase and decrease in profits
    max_increase_index = profit_change_list.index(max(profit_change_list))
    max_decrease_index = profit_change_list.index(min(profit_change_list))

    # Print the financial analysis results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit:,.2f}")
    print(f"Average Revenue Change: ${avg_revenue_change:.1f}")
    print(f"Greatest Increase in Profits: {months_list[max_increase_index]} ${profit_change_list[max_increase_index]:.0f}")
    print(f"Greatest Decrease in Profits: {months_list[max_decrease_index]} ${profit_change_list[max_decrease_index]:.0f}")

    # Write the results to a text file
    output_path = os.path.join("analysis", "PyBank.txt")
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit}\n")
    file.write(f"Average Change: ${avg_revenue_change}\n")
    file.write(f"Greatest Increase in Profits: {months_list[max_increase_index]} (${profit_change_list[max_increase_index]:.0f})\n")
    file.write(f"Greatest Decrease in Profits: {months_list[max_decrease_index]} (${profit_change_list[max_decrease_index]:.0f})")

