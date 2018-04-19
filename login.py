#本程序实现爬虫的自动登录
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

params = {'firstname':'zjlyyq','lastname':'296675700'}
serverAddress = 'http://pythonscraping.com/pages/files/processing.php'    #这是本书教程上的的地址
r = requests.post(serverAddress,params)
print(r.text)

