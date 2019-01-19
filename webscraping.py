"""
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi import pandas as pd
"""
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame

link = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
data = requests.get(link).text

sp = BeautifulSoup(data,"lxml")
#print (sp.prettify())

my_tab = sp.find('table',class_="table")

A1=[]
A=[]
B=[]
C=[]
D=[]

for row in my_tab.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)>0:
        A1.append(str(cells[0].find(text=True)))
        A.append(str(cells[1].find(text=True)))
        B.append(str(cells[2].find(text=True)))        
        C.append(str(cells[3].find(text=True)))
        D.append(str(cells[4].find(text=True)))

df=DataFrame()
df['Rank']=A1
df['Team Name']=A
df['Matches']=B
df['Points']=C
df['Rating']=D


