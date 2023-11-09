# 자바스크립트와 같이 타입(자료형)을 섞어 쓸 수 있음
list = [1, 2, 3 , 'adsfasdf', [4,5,6]]
print(list)
print(list[3])
print(list[4][2])

print("=" * 50)
# - 마이너스 인덱스는 뒤에서 부터 계산
# 앞은 0,1,2,3 ... , 뒤는 -1, -2, -3...
print(list[-1])
print(list[-1][-2])
# 문자열도 인덱스로 찾기 가능
print(list[-2][-2]) 

print("=" * 50)
a = [1,2,3,4,5]
print(a[0:3]) # 이상 : 미만
print(a[0:4:2]) # 이상 : 미만 : 건너뛰기
print(a[::2])
print("=" * 50)

# 반복
print(a*3)
print(len(a))


print("=" * 50)

# 삭제
a = [1,2,3]
del a[1]
print(a)
a = [1,2,3,4,5]
del a[2:]
print(a)

print("=" * 50)

# 메소드
b = [1, 2, 3]
print(b)
b.append(4)
print(b)
print("=" * 50)

# 정렬
a = [1, 4, 3, 2]
a.sort()
print(a)
a = [1, 4, 3, 2]
a.reverse()
print(a)
a = [1, 4, 3, 2]
a.sort()
a.reverse()
print(a)
print("=" * 50)

#insert
a = [1,2,3]
a.insert(1,4)
print(a)
print("=" * 50)

#extend
a = [1, 2, 3]
a.extend([4, 5])
print(a)