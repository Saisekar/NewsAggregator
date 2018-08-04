import quandl
import numpy as np
import csv

#Get the stock from the list text file
lines = [line.rstrip('\n') for line in open('C:\Anaconda\programs\Stock_Market_ML\stock_list.txt')]
stock_count = len(lines)
print (stock_count)

#Open a CSV file for storing all the filtered 50 DMA stocks
csvout = csv.writer(open("filtered_200DMA_080118.csv", "w"))

#Iterate and fire request for every stock
for stock in lines:
    try:
        print (stock)
        data = quandl.get("NSE/"+stock, trim_start = "2015-12-12", trim_end = "2018-07-24", authtoken="1yTmBisER1N75aeV1Ah-")
        diff = (data.Close.tail(1) - ((data.Close).rolling(window=200).mean().tail(1)))/data.Close.tail(1)
        # Check if the stock price is close to 200 DMA
        if ((((diff * 100) > -5).bool()) == True and (((diff * 100) < 5).bool()) == True):
            csvout.writerow((stock, (((diff*100).to_string(index=False).split("\n"))[1])))
    except:
        pass