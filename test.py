from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://pythonscraping.com/pages/cookies/profile.php')
print(html.read())