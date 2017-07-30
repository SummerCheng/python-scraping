#!/usr/bin/python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html.read())
# print(bsObj.head)
print(bsObj.h1)
