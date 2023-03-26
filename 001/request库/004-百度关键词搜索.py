import requests
keyword = input()
try:
    kv = {'wd': keyword}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.50',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
    r = requests.get("https://www.baidu.com/s",params=kv,headers=headers)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('error!')