import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import os
from fake_useragent import UserAgent
import time,random

ua = UserAgent()
def getTags():
    url='https://book.douban.com/tag/?view=cloud'
    response = urllib.request.urlopen(url)
    page = response.read().decode('utf-8')
    soup=BeautifulSoup(page,'html.parser')
    tags=[]
    for book in soup("td"):
        tags.append(book.a.get_text())
    return tags
def visitUsingHeader(url):
    header={"User-Agent":ua.random}#using random headers
    req=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(req)
    page=response.read().decode('utf-8')
    soup=BeautifulSoup(page,'html.parser')
    return soup

f=open('book.csv','w')
tags=getTags()
for tag in tags[1:]:
    ty='T'
    subject=urllib.parse.quote(tag)
    for start in range(0,40,20):
        url='https://book.douban.com/tag/%s?start=%d&type=%s'%(subject,start,ty)
        print(url)
        time.sleep(5)
        soup=visitUsingHeader(url)
        for book in soup("div",class_="info"):
            if book==None or book.find("span",class_="rating_nums")==None or book.find("span",class_="rating_nums").get_text()=='': continue
            score=float(book.find("span",class_="rating_nums").get_text())
            if score >= 9.5:
                print(book.a['title'],score,subject)
                f.write("%s,%f,%s\n"%(book.a['title'],score,tag))
f.close()
