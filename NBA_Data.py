import requests
import pandas as pd
from bs4 import BeautifulSoup
import re


urls = ['https://www.basketball-reference.com/boxscores/202403010BOS.html']

for url in urls:
    html = requests.get(url).text.replace('<!--', '').replace('-->', '')
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table', {'id': re.compile('box-.*-game-basic|box-.*-game-advanced')})
    
    dfs = pd.read_html(str(tables), header = 1)
    
    for df in dfs:
        print(df)

        