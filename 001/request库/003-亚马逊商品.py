from urllib import request
import requests
url = "https://www.amazon.cn/dp/B09DYPG37W/ref=sr_1_7?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=VYLPJ00UTO4U&keywords=%E5%AF%8C%E5%A3%AB&qid=1661828598&sprefix=%E5%AF%8C%E5%A3%AB%2Caps%2C98&sr=8-7&th=1"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)

except:
    print("failed!")