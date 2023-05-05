import csv
with open(r"C:/Users/elias/OneDrive/Desktop/Data Science bootcamp/week_4/Python_challenge/pybank/Resource/budget_data.csv",'r') as file:


    reader = csv.reader(file)
    total_month = 0
    net_profit_loss = 0
    total_change = 0
    previous_month = 0
    row_tracker = 2
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_date = ""
    greatest_decrease_date = ""

    next(reader)  # skip header row
    for row in reader:
        total_month += 1
        net_profit_loss = net_profit_loss + (int(row[1]))
        if row_tracker > 2:
            change_bet_month = (int(row[1])-previous_month)
            total_change = total_change + change_bet_month
            if change_bet_month > greatest_increase:
                greatest_increase = change_bet_month
                greatest_increase_date = row[0]
            if change_bet_month < greatest_decrease:
                greatest_decrease = change_bet_month
                greatest_decrease_date = row[0]
        row_tracker = row_tracker + 1
        previous_month = int(row[1])
    average_change = total_change / (total_month - 1)

print(f"Total months: {total_month}")
print(f'Total: ${net_profit_loss}')
print(f'average_change: ${average_change}')
print(greatest_increase_date,greatest_increase)
print(greatest_decrease_date,greatest_decrease)
# Export the results to a text file
with open(r"C:/Users/elias/OneDrive/Desktop/Data Science bootcamp/week_4/Python_challenge/pybank\Analysis/budget_data.txt", "w") as file:
    file.write(f'Financial Analysis\n')
    file.write('-------------------------------------\n')
    file.write(f"Total Months: {total_month}\n")
    file.write(f"Total: ${net_profit_loss}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f'Greatest Increase in Profit: {greatest_increase_date} (${greatest_increase})\n')
    file.write(f'Greatest Decrease in Profit: {greatest_decrease_date} (${greatest_decrease})\n')