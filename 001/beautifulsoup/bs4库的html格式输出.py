from operator import ge
import requests
r = requests.get("https://python123.io/ws/demo.html")
r.encoding = r.apparent_encoding
#print(r.text)
demo = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')
print(soup.prettify())
