#通过维基百科六度分隔理论，从科比页面出发，找到麦迪
#coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import  re

kobe_url = 'https://zh.wikipedia.org/wiki/%E7%A7%91%E6%AF%94%C2%B7%E5%B8%83%E8%8E%B1%E6%81%A9%E7%89%B9'

def getBs4Obj(url):
    html = urlopen(url)
    return BeautifulSoup(html)

bsObj = getBs4Obj(kobe_url)
for link in bsObj.find('div',{'id':'bodyContent'}).findAll('a',{'href':re.compile('^(/wiki/)((?!:).)*$')}):
    print(link)
