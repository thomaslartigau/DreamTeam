# coding: utf-8

# usage: python DC-roster.py -m "{\"teams\": [\"BOS\", \"GSW\"], \"isRegen\": false}"

import pandas as pd
import requests
from lxml import html
import json
import re
import argparse
from datetime import datetime
import os


def get_url(team):
  return("https://www.basketball-reference.com/teams/" + str(team) +"/2019.html")

def get_file_name(team):
  return("rosters/" + team + "_roster.csv")

def get_metadata(tableName):
  with open('metadata/tables-metadata.json') as f:
    metadatas = json.load(f)
  return(metadatas[tableName])

def get_team_roster(team):
  url = get_url(team)
  page = requests.get(url)
  html_tree = html.fromstring(page.content)
  today = datetime.utcnow().strftime("%Y-%m-%d")

  # Get player ID
  playerID = html_tree.xpath("//table[@id='roster']/tbody/tr/td[1]/a/@href")
  playerID = [re.findall(r"/([a-z0-9]*).html", playerID)[0] for playerID in playerID]

  # Build roster dataframe
  roster = pd.DataFrame(playerID, columns = ["PlayerID"])
  roster["Team"] = team
  roster["Date"] = today

  # Write in CSV
  filename = get_file_name(team)
  if os.path.isfile(filename):
    roster.to_csv(filename, index = False, index_label = False, mode='a', header = False)
  else:
    roster.to_csv(filename, index = False, index_label = False)

  return(roster, None)

def get_message():
  parser = argparse.ArgumentParser(description='Get teams rosters from Basket-Reference')
  parser.add_argument('-m', '--message', help='Input JSON message')
  args = parser.parse_args()
  if args.message :
    return(args.message)
  else :
    return None

def handleMessage(message):
  try:
    print(message)
    message_json = json.loads(message)
    dates = message_json["teams"] if message_json["teams"] else None
    isRegen = message_json["isRegen"]
    return(dates, isRegen)
  except :
    raise Exception("Can't handle message.")

if __name__ == '__main__':
  TEAMS = ["GSW"]
  message = get_message()
  teams_message, isRegen = handleMessage(message)
  teams = teams_message if teams_message is not None else TEAMS
  for team in teams :
    roster, exception = get_team_roster(team)
    print(roster.head())
    print("Get roster for team : {}".format(team)) if exception == None else print(str(exception))
