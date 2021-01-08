import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
vf = requests.get(url)
vf.status_code

s = BeautifulSoup(vf.text, 'lxml')

print(s.prettify())

text_article = s.find('div', attrs={'class' : 'content-background'}).find_all('p')

text = [print(i.get_text()) for i in text_article]