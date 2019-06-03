import requests
from bs4 import BeautifulSoup

page = requests.get('https://workey.codeit.kr/orangebottle/index')

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(page.text, 'html.parser')


tels = soup.select(".container .branch .phoneNum")

list = []
for i in tels:
    list.append(i.text)


print(list)