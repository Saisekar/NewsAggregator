import quandl
import numpy as np
import csv

#Get the stock from the list text file
lines = [line.rstrip('\n') for line in open('C:\Anaconda\programs\Stock_Market_ML\stock_list.txt')]
#lines = [line.rstrip('\n') for line in open('C:\Anaconda\programs\Stock_Market_ML\AMARAJABAT.txt')]
stock_count = len(lines)
print (stock_count)

#Open a CSV file for storing all the filtered 50 DMA stocks
#csvout = csv.writer(open("quarter_momentum.csv", "w"))
f=open("Report_momemtum.txt","w+")
#Iterate and fire request for every stock
for stock in lines:
    try:
        data = quandl.get("NSE/"+stock, trim_start = "2017-08-20", trim_end = "2017-11-20", authtoken="1yTmBisER1N75aeV1Ah-")
        data = data.reset_index()
        #print (data['Date'])
        #print (data.Close.head(1))
        if ((data.Close[0] < data.Close[20]) and (data.Close[20] < data.Close[40]) and (data.Close[40] < data.Close[60])):
            print("TRUE")
            print(data.Close[5])
 #           csvout.writerow(stock)
            f.write(stock + "\n")
        #diff = (data.Close.tail(1) - ((data.Close).rolling(window=200).mean().tail(1)))/data.Close.tail(1)
        # Check if the stock price is close to 200 DMA
        #if ((((diff * 100) > -5).bool()) == True and (((diff * 100) < 5).bool()) == True):
         #   csvout.writerow((stock, (((diff*100).to_string(index=False).split("\n"))[1])))
    except:
        pass