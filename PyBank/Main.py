import os
import csv

pybank_csv = r"C:\Users\kamrk\RutgersDataScience\RUTJER201809DATA3\03-Python\Homework\Instructions\PyBank\Resources\budget_data.csv"


# def average_change(revenue):
#     change_per_month = 


#Open and read CSV
with open(pybank_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

# Read the header row first 
    csv_header = next(csvfile)

#declare variables
    monthcount = 0
    netamount = 0
    revenue = 0 
    
    

    for row in csv_reader:
      monthcount += 1
      netamount += int(row[1])
      
     

    print(f'Total Months: {monthcount}')  
    print(f'Total: ${netamount}')
    print(f'Average Change: ${avgchange}')

    

       

        



    








