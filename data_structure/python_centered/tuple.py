tuple1 = ();
tuple2 = (1, 2, 3, 4, 5 );
tuple3 = "a", "b", "c", "d";

print(tuple1);
print(tuple2);
print(tuple3);


#첫번째와 두번째의 차이.

#값만 출력 : 1
print(tuple2[0])

#자료형 그 자체로 출력됨. 같은 값이지만, : (1,)
print(tuple2[:1])

print(tuple3[1:5])

del tuple2
print(tuple2)