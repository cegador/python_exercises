# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

def getting_titles(file_name):
  url = 'https://www.nytimes.com/'
  ny = requests.get(url)
  print(ny.status_code)

  s = BeautifulSoup(ny.text, 'lxml')
  article_title = s.find('div').find_all('h2')

  print('All title from NY\'s home page are: ')
  titles = [i.get_text() for i in article_title]

  file = open("myfile.txt","w") 
  file.writelines(titles) 
  file.close()

if __name__ == "__main__":
    file_name = input('Write the name of the file you want to save article titles: ')
    getting_titles(file_name)
    print('Your file was saved correctly')