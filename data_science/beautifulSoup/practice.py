from bs4 import BeautifulSoup


html_code = """<!DOCTYPE html>
<html>
<head>
    <title>Sample Website</title>
</head>
<body>
<h2>HTML 연습!</h2>

<p>이것은 첫 번째 문단입니다.</p>
<p>이것은 두 번째 문단입니다!</p>

<ul>
    <li>커피</li>
    <li>녹차</li>
    <li>우유</li>
</ul>

<img src='https://i.imgur.com/bY0l0PC.jpg' alt="coffee"/>
<img src='https://i.imgur.com/fvJLWdV.jpg' alt="green-tea"/>
<img src='https://i.imgur.com/rNOIbNt.jpg' alt="milk"/>

</body>
</html>"""

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(html_code, 'html.parser')

# type 출력
print(type(soup))

# 모든 <li> 태그 선택하기
li_tags = soup.select('li')

# 결과 출력
print(li_tags)

# 첫 번째 요소 출력하기
print(li_tags[0])

# 첫 번째 요소 type 출력하기
print(type(li_tags[0]))

# 첫 번째 <li> 태그의 텍스트 출력하기
print(li_tags[0].text)


# 빈 리스트 만들기
beverage_names = []

# 텍스트 추출해서 리스트에 담기
for li in li_tags:
    beverage_names.append(li.text)

# 결과 출력
print(beverage_names)