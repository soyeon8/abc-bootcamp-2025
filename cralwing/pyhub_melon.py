import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup

url = "https://pyhub.kr/melon/20231204.html"

res = requests.get(url)
html = res.text
soup = BeautifulSoup("html.parser")
el_list = soup.select("#song-list li")
for el in el_list:
    song_title  = el.sselect_one("h2").text
    song_title +" ".join()