# step 1: install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"


# step 2: get the html

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# step 3: parse the html document
soup = BeautifulSoup(htmlContent, 'html.parser')
imagesUrl = soup.find_all("img")
all_links = set()
for links in imagesUrl:
    all_links.add(url+links['src'])
print(all_links)

# step 4: html tree traversal
