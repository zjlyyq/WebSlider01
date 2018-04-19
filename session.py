import requests

session = requests.session()
url = 'http://pythonscraping.com/pages/cookies/welcome.php'
params = {'username':'zjlyyq','password':'password'}
s = session.post(url,params)
print('Cookies is set to:')
print(s.cookies.get_dict())
print('------------')
print('Going to profile page...')
s = session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(s.text)