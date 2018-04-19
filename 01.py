import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://www.17-53.com/"

htmlObj = urlopen(url)
bsObj = BeautifulSoup(htmlObj.read())

# 输出网页源代码看看
#print(bsObj)
#输出所有链接
print('所有链接如下：')
# 找出所有a元素
a_list = bsObj.findAll('a')
#找出所有target属性为_blank的a元素
a_list_target = bsObj.findAll('a',{"target":"_blank"})
#print(a_list)
for i in a_list_target:
    print(i)

print('所有图片如下')
img_list = bsObj.findAll('img')
for img in img_list:
    img_url='none'
    #输出每个img标签对象的属性字典
    print(img.attrs)
    print(img)
    relative_img_url = img["src"]
    print(relative_img_url)
    complete_img_url = url+relative_img_url;
    print(complete_img_url)

def getBs4Obj(url):
    html = urlopen(url)
    return BeautifulSoup(html.read())

bsObj = getBs4Obj('https://v3.bootcss.com/css/#tables')

# print("打印表格的所有数据行")
# for child in bsObj.find("table",{"class":"table"}).children:
#     print(child)
#
# print("打印表格的出了表头外所有数据行")
# for sibling in bsObj.find("table",{"class":"table"}).thead.next_siblings:
#     print(sibling)