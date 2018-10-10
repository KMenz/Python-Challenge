#Import 
import os
import csv

#Create Input Path
pybank_csv = r"C:\Users\kamrk\RutgersDataScience\RUTJER201809DATA3\03-Python\Homework\Instructions\PyBank\Resources\budget_data.csv"

#declare variables
monthcount = 0
netamount = 0
revenue_change = 0
greatest_change = 0
least_change = 1000000000
average_change = 0
revenue_change_sum = 0
last_month = 0


#Open and read CSV
with open(pybank_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

# Read the header row first 
    csv_header = next(csvfile)

       
#Begin Looping Through CSV
    for row in csv_reader:

        #Calculate Totals
        monthcount += 1
        netamount += int(row[1])
       
       #Find Change In Revenue Per Month, set change = 0 for first month
        if last_month == 0:
            revenue_change = 0
        else:
            revenue_change = int(row[1]) - int(last_month)

        revenue_change_sum += revenue_change

        #Find Greatest Increases and Decreases and Corresponding Dates
        if revenue_change > greatest_change:
            greatest_date = row[0]
            greatest_change = revenue_change
        elif revenue_change < least_change:
            least_date = row[0]
            least_change = revenue_change
        last_month = row[1]

#Calculate Average Change  
average_change = revenue_change_sum / (monthcount - 1)
        


#Print Results
print("FINANCIAL ANALYSIS")
print("---------------------------------")
print(f'Total Months: {monthcount}')  
print(f'Total: ${netamount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase In Profit: {greatest_date} ${greatest_change}')
print(f'Greatest Decrease In Profit: {least_date} ${least_change}')


    

       

        



    








