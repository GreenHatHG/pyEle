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

def findPrice(html, Pricelist, Namelist, number):
    soup = BeautifulSoup(html, "html.parser")
    ulTag = soup.find_all("ul", class_ = "ord_listall qs-cleaar")
    
    for ul in ulTag:
        Namelist.append(ul.find(class_ = "shoname").string)
        Pricelist.append(ul.find(class_ = "price active").string)
        number.append(ul.find(class_ = "kc").string)

def prin(Pricelist, Namelist, number):
    fLen = 30
    Len = 15
    print('|' + '商品'.ljust(fLen) + '|' + '价格'.ljust(Len) + '|' + '库存'.ljust(Len) + '|' + '网址'.ljust(Len)) 
    for i in list(range(0, len(Namelist))):
        print(Namelist[i].ljust(fLen) +  Pricelist[i].ljust(Len) + number[i].ljust(Len) )

def main():
    Pricelist = []
    namelist = []
    number = []
    kamigoUrl = ['http://t.cn/EZXjEzS',]
    for url in kamigoUrl:
        html = getHTML(url)
        findPrice(html, Pricelist, namelist, number)
    prin(Pricelist, namelist, number)
main()

'''
TODO:
    read url from file and classify
    sort the Pricelist and print
    print with a websites
'''
