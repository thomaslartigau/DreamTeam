# coding: utf-8
import urllib2
import pandas as pd
import json
from bs4 import BeautifulSoup

url = "https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=06&day=8&year=2018&type=all"

def get_metadata(tableName):
	with open('metadata/tables-metadata.json') as f:
		metadatas = json.load(f)
	return(metadatas[tableName])

def get_columns_list(metadata):
	metadata["columns"]

try :
	# statDF = pd.read_html(url, attrs={'id': 'stats'})[0]
	# statDF = statDF[statDF.Rk != 'Rk']
	# print(statDF.head())
	# statDF.columns = ['Rk', 'Player', 'Tm', 'Unnamed: 3', 'Opp', 'Unnamed: 5', 'MP','FG', 'FGA', 'FG%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%','ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS','GmSc']
	# statDF = statDF.astype({'PTS': "int"})
	# print(statDF.PTS.sum())
	metadata = get_metadata("DailyStatistics")
	metadata["columns"]
	metadata.sort(key=metadata["columns"]["order"], reverse=True)
	print(m)
except ValueError :
	print "Pas de donnees pour cette date"