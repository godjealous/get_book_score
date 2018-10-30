import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import os
from fake_useragent import UserAgent
ua = UserAgent()


def visitDirectly(url):
    response = urllib.request.urlopen(url)
    page=response.read().decode('utf-8')
    soup=BeautifulSoup(page,'html.parser')
    return soup
def visitUsingHeader(url):
    headers={"User-Agent":ua.random}
    req=urllib.request.Request(url=url,headers=headers)
    response=urllib.request.urlopen(req)
    page=response.read().decode('utf-8')
    soup=BeautifulSoup(page,'html.parser')
    return soup
def visitThroughProxy(url):
    proxy=urllib.request.ProxyHandler({'http':'110.40.13.5:80'}) #find proxy ip in www.xicidaili.com free
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    req=urllib.request.Request(url=url)
    response = urllib.request.urlopen(req)
    page = response.read().decode('utf-8')
    soup=BeautifulSoup(page,'html.parser')
    return soup


url='https://book.douban.com/'
a=visitDirectly(url)
print(a.title)
b=visitUsingHeader(url)
print(b.title)
c=visitThroughProxy(url)
print(c.title)

