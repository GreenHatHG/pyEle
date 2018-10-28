from ele import Ele
import requests
from bs4 import BeautifulSoup

def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def findPrice(url, html, obj):
    soup = BeautifulSoup(html, "html.parser")
    ulTag = soup.find_all("ul", class_ = "ord_listall qs-cleaar")
    for ul in ulTag:
        e = Ele()
        e.setUrl(url)
        e.setName(ul.find(class_ = "shoname").string)
        e.setPrice(ul.find(class_ = "price active").string)
        e.setNumber(ul.find(class_ = "kc").string)
        obj.append(e)


def findUrlSecPrice(url, html, obj):
    soup = BeautifulSoup(html, "html.parser")
    divTag = soup.find_all("div", class_ = "")
    for div in divTag:
        if(div.find('p') and div.find('span') and float(div.find('span').string[1:]) < 8):
            e = Ele()
            e.setUrl(url)
            e.setName(div.find("p").string)
            e.setPrice(div.find("span").string)
      #  e.setNumber(ul.find(class_ = "kc").string)
            obj.append(e)

def prin(obj):
    fLen = 25
    Len = 10
    print('|' + '商品'.ljust(fLen) + '|' + '价格'.ljust(Len) + '|' + '库存'.ljust(Len) + '|' + '网址'.ljust(Len)) 
    for i in obj:
        i.prit(fLen, Len)

def funFir(obj):
    kamigoUrl = ['http://t.cn/EZXjEzS',]
    for url1 in kamigoUrl:
        html = getHTML(url1)
        findPrice(url1, html, obj)

def funSec(obj):
    kamidogUrl = ['http://t.cn/EZCt5kp' , 'http://t.cn/EZCt5kp', 'http://t.cn/EZCTQ8j', 'http://t.cn/EZCHi38', 'http://t.cn/EZCQnEm']
    for urlSec in kamidogUrl:
        html = getHTML(urlSec)
        findUrlSecPrice(urlSec, html, obj)

def main():
    obj = []
    funFir(obj)
    funSec(obj)
    prin(obj)
main()

'''
TODO:
    read url from file and classify
    sort the Pricelist and print
    print with a websites
'''
