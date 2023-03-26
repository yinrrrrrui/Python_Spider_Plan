# encoding = utf-8
import requests
#指定url
url = 'https://www.sogou.com/'
response = requests.get(url = url)
#获取响应数据
page_text = response.text
print(page_text)
#持久化存储
with open('./sogou.html','w',encoding='utf-8') as fp:
    fp.write(page_text)
print('finish!!!')