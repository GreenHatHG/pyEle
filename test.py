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
    Len = 30
    print('|' + '商品'.ljust(Len) + '|' + '价格'.ljust(Len) + '|' + '库存'.ljust(Len)) 
    for i in list(range(0, len(Namelist))):
        print(Namelist[i].ljust(Len) +  Pricelist[i].ljust(Len) + number[i].ljust(Len))

def main():
    Pricelist = []
    namelist = []
    number = []
    #url = 'http://kmg.kamigo.cn/link/63MO6OU70MB6K34I'
   # kamigoUrl = ['http://t.cn/EZXjEzS', 'http://t.cn/EZXHcl3']
    kamigoUrl = ['http://t.cn/EZXE7KV',]
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
