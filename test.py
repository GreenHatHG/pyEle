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

def findPrice(html, Pricelist, namelist):
    soup = BeautifulSoup(html, "html.parser")
    ulTag = soup.find_all("ul")
    
    for ul in ulTag:
        liTag = ul.find_all(class_= 'price active')
        if(len(liTag) != 0):
            namelist.append(ul.find_all(class_ = 'shoname'))

    for ul in ulTag:
        print(ul)
        
    '''
    allPrice = soup.find_all("li",class_="price active")
    allName = soup.find_all("li", class_="price active").find_previous("li")
    for price in allName:
        
        namelist.append(price.previous_sibling)
        Pricelist.append(price.string)
        
        print(price)
   '''
    """
    for i in namelist:
        print(i)
    """
    """
    for i in list(range(0, len(namelist))):
        print(namelist[i] + Pricelist[i])
    """

def main():
    Pricelist = []
    namelist = []
    url = 'http://kmg.kamigo.cn/link/63MO6OU70MB6K34I'
    html = getHTML(url)
    findPrice(html, Pricelist, namelist)

main()

