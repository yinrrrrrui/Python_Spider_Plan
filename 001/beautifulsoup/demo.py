from operator import ge
import requests
from urllib.parse import quote
url = 'https://s.taobao.com/search?q=%E7%9B%B8%E6%9C%BA&suggest=history_1&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&_input_charset=utf-8&wq=&suggest_query=&source=suggest'
demp_url = 'https://python123.io/ws/demo.html'
kv = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
      'Cookie':quote('cna=SGwqGpEaYmECAW64s6vOOojc; t=04dd5038a5e7f417f41bf8c89f0cc3d0; _m_h5_tk=072ba2a4e223d4ca4950b3858e1eca30_1664980147685; _m_h5_tk_enc=d2360ee0eea53e6e1fe2ed180c99110a; xlly_s=1; _samesite_flag_=true; cookie2=16889623731d9c84667d80644e1aa57d; _tb_token_=358eeeb356755; sgcookie=E100z6lsojZvDNhHj/mZmcdZmxY2mXlIb43xJ4dRXc/CKwLRxxOv3omvx3/4pnpBDbQ5IUJBaWsvdIsnoAlKizzbN7WGtA7nFJlB2crHbPofekc=; unb=3359093604; uc3=vt3=F8dCv4SjHBqorolcBgk=&lg2=UIHiLt3xD8xYTw==&nk2=sdrate4PdI6i&id2=UNN4DxTeWcR4DA==; csg=1ab2599b; lgc=\u4F0A\u8299alisa; cancelledSubSites=empty; cookie17=UNN4DxTeWcR4DA==; dnk=yinrrrrr; skt=e0e2ba7fafb2baab; existShop=MTY2NDk3MTQwNg==; uc4=nk4=0@s7/zlxHMpkHj4EHNiZ3l/e5WtEY=&id4=0@UgQwGjdwcE6zSLIFsR32oyYI981J; tracknick=\u4F0A\u8299alisa; _cc_=UtASsssmfA==; _l_g_=Ug==; sg=a4b; _nk_=\u4F0A\u8299alisa; cookie1=UtfXDIe4imh8cMcOBOAeqlIlLqqWtf9tgEYJc+1LL4g=; enc=dT0CLcCAzdIQ4Xc4MsLgBrUcFWeDTJPDX5pbcf/6WyDsmrCx+wCcH5FJRkVf4uoYbP5lvqQcD64sT5G1egQKKg==; mt=ci=70_1; thw=cn; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; uc1=cookie15=W5iHLLyFOGW7aA==&cookie21=V32FPkk/gPzW&cookie14=UoeyChsCGAXIJQ==&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw==&pas=0&existShop=false; JSESSIONID=ED64C934127BD34E94B7D25FB319B5BD; isg=BHV1IHgqegkbnp8oFxqmicvchPEv8ikEo3sUYfeaMew7zpXAv0I51INMGJJ4lUG8; tfstk=c4ulBPtU_0rWZQLKhYaW8LJuhs8OwvSYelEmuQd3NCtFvM1mUiSNVT67nd9PA; l=eBOiRtslL2Infrc2BOfanurza77OSIRYYuPzaNbMiOCP9HCB5W-FW6uQN7T6C3GVh6VXR3oBkVywBeYBqQAonxv92j-la_kmn'),
      #'Referer': quote('https://s.taobao.com/search?q=%E7%9B%B8%E6%9C%BA&suggest=history_1&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&_input_charset=utf-8&wq=&suggest_query=&source=suggest')
      }
r = requests.get(url,headers=kv)
r.encoding = r.apparent_encoding
#print(r.text)
demo = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")
print(soup.prettify)