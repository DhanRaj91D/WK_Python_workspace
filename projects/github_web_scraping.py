import requests
from bs4 import BeautifulSoup as bs

"""This simple web scraping project that gives you information about specific github user using his or her user name you
can see name and profile picture of that user no of repositories ans names and link of all that repositories """

github_user = input('Enter github username : ')
url = 'https://github.com/' + github_user

r = requests.get(url)
soup = bs(r.content, 'html.parser')

profile_image = soup.find('img', {'alt': "Avatar"})['src']
print('Profile photo url : ', profile_image)

name = soup.find('span', {'itemprop': 'name'}).string
print('Name of user :', name)

repo = soup.find('a', {'data-tab-item': 'repositories'}).find('span').string
print('No of repositories available :', repo)

all_repo_link = soup.find('a', {'data-tab-item': 'repositories'})['href']
repo_url = 'https://github.com/' + all_repo_link

repo_r = requests.get(repo_url)
soup_repo = bs(repo_r.content, 'html.parser')

repo_list = soup_repo.find('div', id='user-repositories-list').find('ul').find_all('li')
for i, l in enumerate(repo_list, start=1):
    r_name = l.find('a').string
    r_link = l.find('a')['href']
    r_url = 'https://github.com/' + r_link
    print("{}.{} : {}".format(i, r_name, r_url))
