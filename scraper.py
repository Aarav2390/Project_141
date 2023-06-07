from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

response = requests.get(START_URL)

soup = BeautifulSoup(response.text,'html.parser')

headers=["name","distance","mass","radius"]

star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)



name = []
distance =[]
mass = []
radius =[]

for i in range(1,len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    
star_df = pd.DataFrame(list(zip(name,distance,mass,radius)),columns=[headers])
star_df.to_csv('scrapped_data.csv')