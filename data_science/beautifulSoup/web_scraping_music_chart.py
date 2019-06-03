import requests
from bs4 import BeautifulSoup

page = requests.get('https://workey.codeit.kr/music/index')

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(page.text, 'html.parser')


rank = soup.select("article.rank .rank__order li.list")
#print(rank)
list = []
for i in rank:
    list.append(i.text.strip()[4:])

if(list[9]):
    list[9] = list[9].strip()

print(list)
