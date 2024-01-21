# import module
import requests
import pandas as pd
from bs4 import BeautifulSoup

# link for extract html data


def getdata(url):
	r = requests.get(url)
	return r.text

def getfuelprice():
	htmldata = getdata("https://www.psopk.com/")
	soup = BeautifulSoup(htmldata, 'html.parser')

	# print(htmldata)
	# Declare string var
	# Declare list
	mydatastr = ''
	result = []

	# searching all tr in the html data
	# storing as a string
	table = soup.find_all('p', attrs={'class': 'fptitle'})
	return table[1].text[3:len(table[1].text)-4]

# print(getfuelprice())
