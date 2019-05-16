#해시 테이블. 파이썬에선 딕셔너리로.
dictionary_data = {"name":"curious", "nick":"jeager", "class":"math"}
print(dictionary_data)

#수정
dictionary_data["name"] = "souiruc"
print(dictionary_data)

#하나 지우고
del dictionary_data["name"]
print(dictionary_data)

#해시 테이블 자체를 지우고: 전체 지우고 프린트하면 여기서 에러가 나기 때문에 아래가 실행이 안될것
del dictionary_data
#print(dictionary_data)

print()


dictionary_data_for_clear = {"name":"curious", "nick":"jeager", "class":"math"}
print(dictionary_data_for_clear)

#해시 테이블 안의 요소들을 다 지운다.
dictionary_data_for_clear.clear()
print(dictionary_data_for_clear)