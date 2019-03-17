#Dependencies
import csv
import os
file_path = os.path.join("Resources", "budget_data.csv")
total_months = 0
total_revenue = 0

with open(file_path) as financial_data:
    reader = csv.reader(financial_data)
    # Read the header row
    header = next(reader)
    print(header)
    
    first_data_row = next(reader)
    print(first_data_row)
    total_months = total_months + 1
    print(total_months)
    print(first_data_row[0])
    print(first_data_row[1])
    total_revenue = total_revenue + int(first_data_row[1])


    #starting for loop to begin the rest of the processes
    for row in reader:
        total_months = total_months + 1
        print(row)
        print(total_months)
        total_revenue = total_revenue + int(row[1])
        print(total_revenue)

print("End of Program")
