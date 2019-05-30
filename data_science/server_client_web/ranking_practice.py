import requests
from requests.exceptions import HTTPError

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



rating_pages = []
response = []
urlList = makeDomainList(2010, 2018, 12, 5)
print(len(urlList))
for i in urlList:
    #print(i)
    rating_pages.append(requests.get(i).text)
    #print(response.text)
    #print(rating_pages)


print(len(rating_pages))
print(rating_pages[0])


