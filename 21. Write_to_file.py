# Take the code from the How To Decode A Website exercise 
# (if you didn’t do it or just want to play with some different 
# code, use the code from the solution), and instead of printing
#  the results to a screen, write the results to a txt file.
#   In your code, just make up a name for the file you are saving to.

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

  file = open(file_name,"w") 
  file.writelines(titles) 
  file.close()

if __name__ == "__main__":
    file_name = input('Write the name of the file you want to save article titles: ')
    getting_titles(file_name)
    print('Your file was saved correctly')