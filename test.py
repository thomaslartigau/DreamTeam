# coding: utf-8

# usage: python3 test.py -m "{\"dates\": [\"2018-10-29\", \"2018-10-21\"], \"isRegen\": false}"

import pandas as pd
import requests
from lxml import html
import json
import re
import argparse
from datetime import datetime


def get_url(day, month, year):
	return("https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=" + str(month) + "&day=" + str(day) + "&year=" + str(year) + "&type=all")

def get_file_name(day, month, year):
	return("daily_statistics/" + str(year) + "-" + str(month) + "-" + str(day) + "_daily_statistics.csv")

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

def get_title_date(html_tree):
	page_title = html_tree.xpath("//div[@id='content']/h1")[0].text
	date_title = re.findall(r"NBA Daily Stats Leaders for ([a-zA-Z]* [0-9]{1,2}, [0-9]{4})|$", page_title)[0].lower()
	date = datetime.strptime(date_title, "%B %d, %Y")
	return(date.year, date.month, date.day)

def get_daily_stats(year, month, day):
	try :
		metadata = get_metadata("DailyStatistics")
		url = get_url(day, month, year)
		page = requests.get(url)
		html_tree = html.fromstring(page.content)

		title_year, title_month, title_day = get_title_date(html_tree)
		if title_year == year and title_month == month and title_day == day :
			statDF = pd.read_html(url, attrs={'id': 'stats'})[0]
			statDF.columns = get_columns_list(metadata)

			# Process the data
			statDF = statDF[statDF.Rk != 'Rk']
			statDF["MP"] = [process_minute(minute) for minute in statDF["MP"].values]
			statDF = statDF.astype(get_columns_type_dict(metadata))

			# Compute evaluation
			statDF["Evaluation"] = compute_evaluation(statDF)

			# Get Player ID
			statDF["PlayerID"] = html_tree.xpath('//*[@id="stats"]/tbody/tr/td[1]/a/@href')
			statDF["PlayerID"] = [re.findall(r"/([a-z0-9]*).html", playerID)[0] for playerID in statDF["PlayerID"].values]

			statDF.to_csv(get_file_name(day, month, year), index = False, index_label = False)
			return(statDF, None)

		else :
			return(None, Exception("No data for this date : " + str(year) + "-" + str(month) + "-" + str(day)))

	except ValueError :
		return(None, Exception("Error when crawling date: " + str(year) + "-" + str(month) + "-" + str(day)))

def get_message():
	parser = argparse.ArgumentParser(description='Get daily statistics from Basket-Reference')
	parser.add_argument('-m', '--message', help='Input JSON message', required=True)
	args = parser.parse_args()
	if args.message :
		return(args.message)
	else :
		raise Exception("No message found")

def handleMessage(message):
	try:
		message_json = json.loads(message)
		dates = message_json["dates"]
		isRegen = message_json["isRegen"]
		return(dates, isRegen)
	except :
		raise Exception("Can't handle message.")

def get_detailed_date(date_str):
	date = datetime.strptime(date_str, "%Y-%m-%d")
	return(date.year, date.month, date.day)


if __name__ == '__main__':
	message = get_message()
	dates, isRegen = handleMessage(message)
	for date in dates :
		year, month, day = get_detailed_date(date)
		daily_stat, exception = get_daily_stats(year, month, day)
		print("Get daily stats for date : {}-{}-{}".format(year, month, day)) if exception == None else print(str(exception))
