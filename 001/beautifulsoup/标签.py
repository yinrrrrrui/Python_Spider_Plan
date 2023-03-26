import requests
from bs4 import BeautifulSoup
r = requests.get("https://python123.io/ws/demo.html")
r.encoding = r.apparent_encoding
#print(r.text)
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
tag = soup.p
print(tag)