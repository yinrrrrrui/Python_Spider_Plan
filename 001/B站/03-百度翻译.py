from email import header
from boto import UserAgent
import requests
import json

from sqlalchemy import false
#录入单词后页面内容会进行局部刷新
post_url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
word = input('enter a word:')
data = {
    'kw': word
}
response = requests.post(url=post_url,data=data,headers=headers)
#直接返回obj（对象），确认响应数据是json类型才可以
dic_obj= response.json()
print(dic_obj)
filename = word + '.json'
fp = open(filename,'w',encoding='utf-8')
#中文不能使用ensure_ascii
json.dump(dic_obj,fp=fp,ensure_ascii=false)
print('finish!!!')