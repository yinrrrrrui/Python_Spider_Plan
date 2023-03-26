import requests
try:
    kv = {'user-agent':'Mozilla/5.0'}
    url = 'https://www.ip138.com/iplookup.asp?ip='
    r = requests.get(url + '221.237.85.171'+'&action=2',headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('error!')