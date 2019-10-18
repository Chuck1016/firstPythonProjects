##  from YouTube tutorial: CSV Files In Python by Socratica

import csv, datetime

# import csv file and read it into a variable
# the function and argument are run each time the reader variable is called

path = "/home/chuck/Documents/GoogleStockMarketData.csv"
file = open(path, newline='')
reader = csv.reader(file)

# separate header from data
# since nothing has run yet, the'next' line in the file will be the header row

header = next(reader)

# each i of the for loop will run the reader() and assign the result the nane row
# then assign the correct datatype to each value in row based on index position
# then append these variables to the empty list in order

data = []
for row in reader:
    date = datetime.datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])
    data.append([date, open_price, high, low, close, volume, adj_close])

# create a destination file, then put the results into a writer variable
# loop row from that variable into the new file
# for loop only returning the date and price dif between open & close (return)

return_path = "/home/chuck/Documents/GoogleReturns.csv"
file = open(return_path, 'w')
writer = csv.writer(file)

# enter literal strings for header row

writer.writerow(["Date", "Return"])

# loop range = # or rows -1 (header)

for i in range(len(data)-1):
    todays_row = data[i]            # current row
    todays_date = todays_row[0]     # first position of current row
    todays_price = todays_row[-1]   # last position of the current row
    yesterdays_row = data[i+1]      # + not - because the dates are desc
    yesterdays_price = yesterdays_row[-1]

# math for the % diff from yesterday to today

    daily_return = round((todays_price - yesterdays_price) / yesterdays_price, 4)
    form_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([form_date, daily_return])
    





