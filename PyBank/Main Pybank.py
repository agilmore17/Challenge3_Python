#modules
import os
import csv

#setup file path, must start in PyBank folder
pybank_csv = os.path.join('Resources','budget_data.csv')

#formatting
print("Financial Analysis")
print("________________________________")
print("")

#setup empty arrays to allow for data to be stored
date = []
profit_loss = []

#open the file & store it as a list
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        date.append(row[0])
        profit_loss.append(row[1])


#find length
print("Total Months: " + str(len(date)))


#net profit / loss
int_profit_loss = [int(x) for x in profit_loss]

print("Total: $" + str(sum(int_profit_loss)))


#average change of profit / loss
def Average(x):
    return sum(x) / len(x)

average = Average(int_profit_loss)

print("Average Change: $" + str(round((average))))


#greatest increase in profits (date and amount)

max_profit = max (int_profit_loss)

dict(zip(int_profit_loss, date))
pandl_dict = dict(zip(date, int_profit_loss))

#print(max(pandl_dict, key=pandl_dict.get)) ended up using a .get function after some research and just combining it with the max of other array

print("Greatest Increase in Profits: " + (max(pandl_dict, key=pandl_dict.get) + " " + "($" + str(max_profit) + ")" ))

#greatest decrease in profits (date and amount)

min_profit = min(int_profit_loss)

print("Greatest Decrease in Profits: " + (min(pandl_dict, key=pandl_dict.get) + " " + "($" + str(min_profit) + ")"))

#write to text file, creating 2 new folders if they do not exist already

with open ('PyBank Solution', 'w') as txtfile:
    txtfile.write("Financial Analysis\n ___________________")
    txtfile.write("\nTotal Months: " + str(len(date)))
    txtfile.write("\nTotal: $" + str(sum(int_profit_loss)))
    txtfile.write("\nAverage Change: $" + str(round((average))))
    txtfile.write("\nGreatest Increase in Profits: " + (max(pandl_dict, key=pandl_dict.get) + " " + "($" + str(max_profit) + ")" ))
    txtfile.write("\nGreatest Decrease in Profits: " + (min(pandl_dict, key=pandl_dict.get) + " " + "($" + str(min_profit) + ")"))