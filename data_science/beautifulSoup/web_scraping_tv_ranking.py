import requests
from bs4 import BeautifulSoup

# 코드를 작성하세요.

ppp= requests.get('https://workey.codeit.kr/ratings/index?year=2017&month=1&weekIndex=7')
#print(ppp.text)
p1 = ppp.text
ppp1 = requests.get('https://workey.codeit.kr/ratings/index?year=2017&month=1&weekIndex=2')
#print(ppp1.text)
p2 = ppp1.text
# 테스트 코드

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(p1, 'html.parser')
soup1 = BeautifulSoup(p2, 'html.parser')

# 모든 <img> 태그 선택하기
res1 = soup.select('.row')
res2 = soup1.select('.row')
print('s')
print(len(res1))
print('m')
print(len(res2))

#하나 이상인 것만 리스트에 response.text형태로 집어넣는다.

#일단.... 주까지 완성.
def makeDomainList(yearStartNum, yearLastNum, monthNum, weekNum):
    domainList = []
    basic = 'https://workey.codeit.kr/ratings/index?'
    year = 'year='
    month = '&month='
    week = '&weekIndex='
    for yearIdx in range(yearStartNum, yearLastNum + 1):
        for monthIdx in range(1, monthNum + 1):
            for weekIdx in range(weekNum):
                sum = basic + year + str(yearIdx) + month + str(monthIdx) + week + str(weekIdx)
                domainList.append(sum)

    return domainList

data_list = []
urlList = makeDomainList(2010, 2018, 12, 5)
for i in urlList:
    response = requests.get(i)
    rating_page = response.text

    soup = BeautifulSoup(rating_page, 'html.parser')
    res = soup.select('.row')
    if len(res) > 1:
        data_list.append(response.text)


print(len(data_list)) # 가져온 총 페이지 수
print(data_list[0]) # 첫 번째 페이지의 HTML 코드