import requests
from bs4 import BeautifulSoup

def getHTML(url):
    try:
        url = 'http://kmg.kamigo.cn/link/63MO6OU70MB6K34I'
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def findPrice(html, Pricelist, namelist):
    soup = BeautifulSoup(html, "html.parser")
    allPrice = soup.find_all(class_="price active")
    allName = soup.find_all(class_="shoname")

    for price in allPrice:
        Pricelist.append(price.string)
    
    for name in allName:
        namelist.append(name.string)

def main():
    Pricelist = ()
    namelist = ()
    url = 'http://kmg.kamigo.cn/link/63MO6OU70MB6K34I'
    html = getHTML(url)
    findPrice(html, Pricelist, namelist)

main()

