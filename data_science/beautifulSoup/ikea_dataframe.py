import pandas as pd
import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
records = []

# 시작 페이지 지정
page_num = 1

while True:
    # HTML 코드 받아오기
    response = requests.get("https://www.ikea.com/kr/ko/search/?query=desk&pageNumber=" + str(page_num))

    # BeautifulSoup 타입으로 변형하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # "prodName" 클래스가 있을 때만 상품 정보 가져오기
    if len(soup.select('.prodName')) > 0:
        product_names = soup.select('.prodName')
        product_prices = soup.select('.prodPrice')
        product_urls = soup.select('.prodImg')
        page_num += 1

        # 상품의 정보를 하나의 레코드로 만들고, 리스트에 순서대로 추가하기
        index = 0
        for name in product_names:
            record = []
            record.append(product_names[index].text)
            record.append(product_prices[index].text.strip())
            record.append("https://www.ikea.com" + product_urls[index].get('src'))
            records.append(record)
            index += 1
    else:
        break;

# DataFrame 만들기
df = pd.DataFrame(data=records, columns=["이름", "가격", "이미지 주소"])

# DataFrame 출력
print(df.head())
