import requests
from requests.exceptions import HTTPError


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




print(len(makeDomainList(2010, 2018, 12, 5)))

#list for url:
url = ['https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0',
       'https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=1',
       'https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=2',
       'https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=3',
       'https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=4']

data_list = []
urlList = makeDomainList(2010, 2018, 12, 5)
for i in urlList:
    try:
        response = requests.get(i)
        rating_pages = response.text
        data_list.append(rating_pages)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:

        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')


print(len(data_list)) # 가져온 총 페이지 수
print(data_list) # 첫 번째 페이지의 HTML 코드