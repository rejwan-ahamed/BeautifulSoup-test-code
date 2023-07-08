import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

filterImages = soup.find_all('img')

singleImageLinks = set()
for links in filterImages:
    # print(links['src'])
    singleImageLinks.add(url+links['src'])

print(singleImageLinks)    
