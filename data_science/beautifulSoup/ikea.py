import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
pages = []

# 첫 페이지 번호 지정
page_num = 1

while True:
    # HTML 코드 받아오기
    response = requests.get("https://www.ikea.com/kr/ko/search/?query=desk&pageNumber=" + str(page_num))

    # BeautifulSoup 타입으로 변환하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # ".prodName" 클래스가 있을 때만 HTML 코드를 리스트에 담기
    if len(soup.select('.prodName')) > 0:
        pages.append(soup)
        page_num += 1
    else:
        break;

# 가져온 페이지 개수 출력하기
print(len(pages))

print(pages)