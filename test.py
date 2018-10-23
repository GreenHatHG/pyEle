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

def findPrice(html):
    soup = BeautifulSoup(html, "html.parser")
    print(soup)

def main():
    url = 'http://kmg.kamigo.cn/link/63MO6OU70MB6K34I'
    html = getHTML(url)
    findPrice(html)
main()

