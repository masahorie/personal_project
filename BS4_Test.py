from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd

url = "https://news.yahoo.co.jp"
response = urlopen(url)

parse_html = BeautifulSoup(response,'html.parser')

title_lists=parse_html.find_all('a')

title_list=[]
url_list=[]

for i in title_lists:
    title_list.append(i.string)
    url_list.append(i.attrs['href'])

df_title_url = pd.DataFrame({'Title':title_list, 'URL':url_list})

df_contain_python = df_notnull = df_title_url.dropna(how='any')

# df_contain_python = df_notnull[df_notnull['Title'].str.contains('Python超入門コース')]

df_contain_python.to_csv('output1.csv')