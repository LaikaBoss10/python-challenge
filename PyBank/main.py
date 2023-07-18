# Module for creating file paths
import os
# Module for reading CSV files
import csv

#make path variable to direct the csv open
budget_csvpath = os.path.join("Resources", "budget_data.csv")

#lists to store data
Date =  []
ProfitLoss = []
Change = []


#open the budget csv
with open(budget_csvpath) as budgetcsv:
    #read the budget csv
    csvreader = csv.reader(budgetcsv,delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        #fill the values of the date list and profit loss list from the csv data
        Date.append(row[0])
        ProfitLoss.append(int(row[1]))
#fill values from the change list by subtracting each profitloss from the next profit loss.
# List is 1 point shorter than the profit loss list
for i in range(len(ProfitLoss)):
    if i < len(ProfitLoss)-1:
        Change.append(ProfitLoss[i+1]-ProfitLoss[i])

#calulate net profit by taking a sum of profit loss
NetProfit = sum(ProfitLoss)
#calculate average change
AverageChange = sum(Change)/len(Change)

#calculate max and min change, and use index to find the date of the max and min change
MaxChange = max(Change)
DateMaxChange = Date[Change.index(max(Change))+1]
MinChange = min(Change)
DateMinChange = Date[Change.index(min(Change))+1]


#All print statements to send results to the terminal in the appropriate format
print("Financial Analysis\n")
print("----------------------------\n")
print("Total Months: " + str(len(Date)))
print()
print(f"Total: ${NetProfit}\n")
print(f"Average Change: ${AverageChange:.2f}\n")
print(f"Greatest Increase in Profits: {DateMaxChange} (${MaxChange})\n")
print(f"Greatest Decrease in Profits: {DateMinChange} (${MinChange})\n")

#set path and name of output txt file
output_path = os.path.join("analysis", "Pybank_Output.txt")

#write to output path
with open(output_path, 'w') as txtfile:
    #writes the f string format it the txt file following the appropriate format guidelines
    txtfile.write(f"Financial Analysis\n\n----------------------------\n\nTotal Months: {len(Date)}\n\nTotal: ${NetProfit}\n\nAverage Change: ${AverageChange:.2f}\n\nGreatest Increase in Profits: {DateMaxChange} (${MaxChange})\n\nGreatest Decrease in Profits: {DateMinChange} (${MinChange})\n\n")