from lxml import etree
from nbformat import write
from requests import Session
from tqdm import tqdm
import random
import time
#创建一个txt文档并写入爬取到的章节内容
#因为所有的url是连续的
def txtCreate(titleXpath,treeXpath,fullPath):
    file = open(fullPath,'a',encoding="utf-8")
    file.writelines(titleXpath[0])
    for i in range(len(treeXpath)):
        #print(treeXpath[i])  打印文本内容的注释
        file.writelines(treeXpath[i])
        file.write('\n')
    file.write('\n')
    file.close()
    print('finish write!')
    return

#parser = etree.HTMLParser(encoding='utf-8')
#,parser=parser
#url = 'https://www.cascoo.net/141_141746/85024209.html'
#第二章url每一章内容的xpath都一样

#创建一个爬取的文件
Path = 'D:/code/爬虫/xpath解析方法'
txtName = input()
fullPath = Path + '/' + txtName + '.txt'
url = 'https://www.cascoo.net/141_141746/'#'85024209.html
#实例化sesion对象
for i in tqdm(range(85024209,85024462)):
    url_new = (url + '{}' + '.html').format(i)
    print(url_new)
    #requests.session的作用：自动处理cookie，即下一次请求会带上前一次的cookie
    session = Session()
    pageContent = session.get(url_new).content.decode("utf-8")
    tree = etree.HTML(pageContent)
    #/text()会获取标签中直系的文本内容  //text()会获取标签中非直系的文本内容
    #爬取文件内容和文章标题
    title_tree = tree.xpath('/html/body/div/div[5]/div/div[2]/h1/text()')
    page_tree = tree.xpath('/html/body/div/div[5]/div/div[3]/text()')
    txtCreate(title_tree,page_tree,fullPath)
    print('finish xpath!')
    #随机休眠
    t = random.randint(1, 5)  
    time.sleep(t)
