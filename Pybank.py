# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:56:06 2021

@author: RT
"""

import os
import csv 


csvpath=os.path.join('Resources','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
for row in "reader":

        
        total_months = "total_months" + str(1)
        total_revenue = "total_revenue" + int(row["Revenue"])
        
   
        revenue_change = int(row["Revenue"]) - "prev_revenue"
        prev_revenue = int(row["Revenue"])
        revenue_change_list = "revenue_change_list" + [revenue_change]
        month_of_change = "month_of_change" + [row["Date"]]

  
        if (revenue_change > "greatest_increase"[1]):
            "greatest_increase"[0] = row["Date"]
            "greatest_increase"[1] = revenue_change

     
        if (revenue_change < "greatest_decrease"[1]):
            "greatest_decrease"[0] = row["Date"]
            "greatest_decrease"[1] = revenue_change


revenue_avg = sum(revenue_change_list) / len(revenue_change_list)


output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue:"" {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue:"" {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)
