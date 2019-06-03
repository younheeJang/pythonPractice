import pandas as pd
import requests
from bs4 import BeautifulSoup


res = requests.get('https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0')

res = res.text

#print(res)

# BeautifulSoup 타입으로 변형하기
soup = BeautifulSoup(res, 'html.parser')

#각 필요한 데이터를 컬럼 형식으로 넣기 위한 전처리단계;
#step1: 각 컬럼으로 들어갈 데이터들을 가진 노드들을 분리해서 뽑는다
node_period = soup.select('#weekSelectBox option')
node_rank = soup.select('tr.row td.rank')
node_channel = soup.select('tr.row td.channel')
node_program = soup.select('tr.row td.program')
node_percent = soup.select('tr.row td.percent')

data_period = []
data_rank = []
data_channel = []
data_program = []
data_percent = []



def for_in_statement(list):
    data_list = []
    for i in list:
        data_list.append(i.text)
        print(data_list)
    return data_list


#print(for_in_statement(node_period))
data_period  = []
for i in range(0,10):
    data_period.append('2009.12.28 ~ 2010.01.03')
data_rank = for_in_statement(node_rank)
data_channel = for_in_statement(node_channel)
data_program = for_in_statement(node_program)
data_percent = for_in_statement(node_percent)
print(node_percent)
print(data_percent)


records = {"period":data_period, "rank":data_rank, "channel":data_channel, "program":data_program, "rating":data_percent}
# DataFrame 만들기
df = pd.DataFrame(data=records)

# DataFrame 출력
print(df.head())



