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

def getUrlList():
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
    for i in tqdm(range(1,75)):
        #//*[@id="booklist"]/li[1]/a
        #//*[@id="booklist"]/li[74]/a、
        #为了获得标签中的href其每一页具体的网址
        xpath_url = ('//*[@id="booklist"]/li[{}]/a/@href').format(i)
        use_url = tree.xpath(xpath_url)
        url_list.append(use_url[0])
        time.sleep(0.3)
    print(url_list)
    print("爬取的章节总数为%d"%len(url_list))
    print('爬取书目录url完成')
    return url_list

#@retry(stop_max_attempt_number=5,wait_fixed=2000,stop_max_delay=20000)
#创建一个txt文档并写入爬取到的章节内容
def txtCreate(titleXpath,treeXpath,fullPath):
    file = open(fullPath,'a',encoding="utf-8")
    file.writelines(titleXpath[0])
    file.write('\n')
    for i in range(len(treeXpath)):
        #print(treeXpath[i])  打印文本内容的注释
        file.writelines(treeXpath[i])
        #file.write('\n')
        #file.write('\n')
    file.write('\n')
    file.close()
    #print('finish write!')
    return

@retry(stop_max_attempt_number=5,wait_fixed=2000,stop_max_delay=20000)
def getPage(url):
    content = requests.get(url=url,headers=headers,timeout=25)
    content.encoding = 'utf-8'
    return content

#创建一个爬取的文件
Path = 'D:/code/爬虫/xpath解析方法'
txtName = input()
fullPath = Path + '/' + txtName + '.txt'

#获得需要爬取的url_list
url_list= getUrlList()
print('开始爬取小说！')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.2242 SLBChan/10',
    'Connection': 'close'
    }
proxies = {
        'http': '127.0.0.1:1212',
        'https': '127.0.0.1:1212'
    }
for i in tqdm(range(0,len(url_list))):
    url = 'https://www.wmdown8.com' + url_list[i]
    try:
        #写一个函数加入重做模块
        content = getPage(url)
    except:
        print('页面获取失败')
    tree = etree.HTML(content.text)
    titleXpath = tree.xpath('//div[2]/h1/text()')
    treeXpath = tree.xpath('//div[2]/div[2]/text()')
    txtCreate(titleXpath,treeXpath,fullPath)
    #print('finish xpath!')
    #随机休眠
    t = random.randint(1, 3)  
    time.sleep(t)
print('恭喜完成小说的爬取！')

'''
    request = urllib.request.Request(url=url,headers=headers)
    # 发送请求访问服务器，返回响应对象
    response = urllib.request.urlopen(request)
    # 解码响应对象，得到页面源码
    content = response.read().decode('utf-8',"ignore")
    
    session = Session()
    content = session.get(url).content.decode("utf-8")
    '''




