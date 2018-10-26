import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import os

url='https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
response = urllib.request.urlopen(url)
page = response.read().decode('utf-8')
soup=BeautifulSoup(page,'html.parser')
tags=[]
for book in soup("td"):
    tags.append(book.a.get_text())
f=open('tag.txt','w')
f.writelines(tags)
f.close()
print(tags,len(tags))

