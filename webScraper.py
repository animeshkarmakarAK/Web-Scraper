import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Web_crawler')
print( type(res))
soup = bs4.BeautifulSoup(res.text, 'html')
print(type(soup))
headline = soup.select('.mw-headline')
#print(headline)

for i in headline:
    print(i.text)
#now extracting all the links in this page

for link in soup.find_all('a', href = True):
    print(link['href'])
    
