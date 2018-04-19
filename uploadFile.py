#实现文件上传
import requests

files = {'uploadFile':open('images/IMG_4273.jpg','rb')}

r = requests.post('http://pythonscraping.com/pages/processing2.php',files=files)
print(r.text)