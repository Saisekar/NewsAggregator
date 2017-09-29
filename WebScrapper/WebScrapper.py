from bs4 import BeautifulSoup
import requests
import Cleanser.CleanseData
from Cleanser import CleanseData
from time import sleep
import csv
import pandas as pd
import io


#MoneyControl
from docutils.nodes import line

MC_page = requests.get("http://www.moneycontrol.com/news/business/stocks/page-1/")
#Economic Times
ET_page = requests.get("http://economictimes.indiatimes.com/markets/stocks/news")

soup_MC = BeautifulSoup(MC_page.content, 'html.parser')
soup_ET = BeautifulSoup(ET_page.content, 'html.parser')
for a in soup_MC.find_all('a', href=True):
   line = a['href']
   CleanseData.print_func(line[0:])
#for a in soup_ET.find_all('a', href=True):
#	print (a['href'])