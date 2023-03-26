#定向爬虫，只针对给定的URL进行爬取，不进行扩展爬取
from pip import main
import requests
from bs4 import BeautifulSoup
import bs4
#步骤1：从网络上获取大学排名网页内容
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    
    except:
        return ""

#步骤2：提取网页内容中信息到合适的数据结构
def fillUnivlist(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    #对于tbody的子孙tr进行遍历
    #需要过滤掉非标签类型的信息,用isinstance函数来判断
    for tr in soup.find('tbody').children:
        #如果不是bs4.element.Tag类型就过滤掉
        if isinstance(tr,bs4.element.Tag):
            #tr标签已经成功被选取出来，现在需要对tr中的td标签进行提取
            tds = tr('td')
            #需要在ulist中添加相应字段，对应大学排名，对应层次，大学名称，大学分数
            ulist.append([tds[0].text.strip(),tds[2].text.strip(),tds[3].text.strip(),tds[4].text.strip()])

#步骤3：利用数据结构展示并输出结果
def printUnivlist(ulist,num):
    #打印表头
    #右边^表示是这个元素居中，10表示这个元素占用10个空格宽度
    #想要对齐得更加好看需要采用中文字符的空格填充chr(12288)——居中对齐
    tplt = "{0:^10}\t{1:^10}\t{2:{4}^15}\t{3:^10}"
    #{4}表示采用第四个变量进行填充
    print(tplt.format("2022大学排名","层次排名","大学名称","大学分数",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))
    print("Suc" + str(num))
    return

if __name__=="__main__":
        uinfo = []
        url = 'https://www.shanghairanking.cn/rankings/bcsr/2022/0812'
        html = getHTMLText(url)
        fillUnivlist(uinfo,html)
        printUnivlist(uinfo,20) #先打印出20个学校的信息

