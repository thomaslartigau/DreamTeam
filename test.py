# coding: utf-8
#import urllib2
import pandas as pd
import requests
from lxml import html
import json
from bs4 import BeautifulSoup

day = 18
month = 10
year = 2018

def get_url(day, month, year):
	return("https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=" + str(month) + "&day=" + str(day) + "&year=" + str(year) + "&type=all")

def get_file_name(day, month, year):
	return("daily_statistics/" + str(year) + str(month) + str(day) + "_daily_statistics.csv")

def get_metadata(tableName):
	with open('metadata/tables-metadata.json') as f:
		metadatas = json.load(f)
	return(metadatas[tableName])

def get_columns_list(metadata):
	columns = metadata["columns"]
	columns_ordered = sorted(columns, key=lambda c: c["order"])
	columns_list = [ column["columnName"] for column in columns_ordered]
	return(columns_list)

def get_columns_type_dict(metadata):
	columns = metadata["columns"]
	columns_type = {}
	for column in columns :
		columns_type.update({column["columnName"] : column["type"]})
	return(columns_type)

def process_minute(MP) :
	mins = MP.split(":")
	return( float(int(mins[0]) + (1.0 * int(mins[1]) / 60)))

def compute_evaluation(stats) :
	return([0 for player in range(stats.shape[0])])

try :
	metadata = get_metadata("DailyStatistics")
	url = get_url(day, month, year)
	statDF = pd.read_html(url, attrs={'id': 'stats'})[0]
	statDF.columns = get_columns_list(metadata)

	# Process the data
	statDF = statDF[statDF.Rk != 'Rk']
	statDF["MP"] = [process_minute(minute) for minute in statDF["MP"].values]
	statDF = statDF.astype(get_columns_type_dict(metadata))

	# Compute evaluation
	statDF["Evaluation"] = compute_evaluation(statDF)

	print(statDF.head())
	page = requests.get(url)
	#https://docs.python-guide.org/scenarios/scrape/
	tree = html.fromstring(page.content)
	statDF["PlayerID"] = tree.xpath('//*[@id="stats"]/tbody/tr/td[1]/a/@href')
	print(statDF["PlayerID"].values)
	#statDF.to_csv(get_file_name(day, month, year))
except ValueError :
	print("Pas de donnees pour cette date")
