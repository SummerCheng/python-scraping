from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
namelist=bsObj.findAll(text="the prince")

allText = bsObj.findAll(id="text")
print(allText[0].get_text())