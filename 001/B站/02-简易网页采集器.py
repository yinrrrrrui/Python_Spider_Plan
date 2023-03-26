from boto import UserAgent
from pytest import param
import requests
#UA伪装：让爬虫对应的请求身份标识伪装成一款浏览器
#将对应的user-agent封装到字典中
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
}
url = 'https://www.sogou.com/web'
#设置动态url(处理携带参数)
kw = input('enter a word:')
param = {
    'query':kw
}
response = requests.get(url=url,params=param,headers=headers)
response.encoding = 'utf-8'
page_text = response.text
filename = kw+'.html'
with open(filename,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(filename,'保存成功！！！')