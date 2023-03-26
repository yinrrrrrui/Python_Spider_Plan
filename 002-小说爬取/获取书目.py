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
#获得所有章节的url链接

# 用户代理
#用于获取目录即每一章url的总页面
all_url = 'https://www.zongcaixs.cc/edunvpeitajiaomeidongren/'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.2242 SLBChan/10',
'Connection': 'close'

}
# 定制请求头
request = urllib.request.Request(url=all_url,headers=headers)
# 发送请求访问服务器，返回响应对象
response = urllib.request.urlopen(request)
# 解码响应对象，得到页面源码
content = response.read().decode('utf-8',"ignore")
tree = etree.HTML(content)
url_list = [] 
print('开始爬取')
for i in tqdm(range(1,3)):
    #//*[@id="booklist"]/li[1]/a
    #//*[@id="booklist"]/li[74]/a
    #为了获得标签中的href其每一页具体的网址
    xpath_url = ('//*[@id="booklist"]/li[{}]/a/@href').format(i)
    use_url = tree.xpath(xpath_url)
    print(use_url)
    url_list.append(use_url[0])
    time.sleep(0.3)
print(url_list[0])
print("爬取的章节总数为%d"%len(url_list))
print('爬取书目录url完成')

