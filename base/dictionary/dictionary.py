# 딕셔너리 자료형
# 키 : 벨류, hash, map 등

dic = {'name' : 'pey', 'phone' : 123}

print(type(dic))

print("=" * 50)

# 값 추가 
dic[13] = '테스트'
print(dic)

# 값 삭제
del dic['name']
print(dic)

print("=" * 50)

# 키값음 immu 타입만
d2 = {(1,2): '된다?'}
print(d2)

#d3 = {[1,2]: '오류'}
print("=" * 50)


#함수
#keys 파이썬 3.0부터 dict_keys 타입으로 리턴
# list와 거의 비슷하지만 append, insert, pop, remove, sort 등의 함수가 없다.
# 반복문을 위해 키값만 목록으로 내려준다
# 필요시 list()로 형변환한다.

print(dic.keys())
print(list(dic.keys()))

print(dic.values())
print(dic.items())
