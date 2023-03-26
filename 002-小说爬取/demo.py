from lxml import etree
from nbformat import write
from requests import Session
from sympy import content
from tqdm import tqdm
import random
import time
import urllib.request
import requests
from retrying import retry

all_url = 'https://www.wmdown8.com/novel/YjLuo.html'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.2242 SLBChan/10',
'Connection': 'close'

}
# 定制请求头
content = requests.get(url=all_url,headers=headers,timeout=25)
content.encoding = 'utf-8'
print(content.text)
tree = etree.HTML(content.text)
url_list = [] 
print('开始爬取')
for i in tqdm(range(13,114)):
    #/html/body/div[5]/dl/dd[13]/a
    #/html/body/div[5]/dl/dd[113]/a
    #/html/body/div[5]/dl/dd[15]/a
    #/html/body/div[5]/dl/dd[13]/a
    xpath_url = ('//dl/dd[{}]/a/@href').format(i)
    use_url = tree.xpath(xpath_url)
    print(use_url)
    url_list.append(use_url[0])
    time.sleep(0.3)
print(url_list)
print("爬取的章节总数为%d"%len(url_list))
print('爬取书目录url完成')