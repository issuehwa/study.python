# 집합 자료형

s1 = set([1,2,3])
print(s1)
print(type(s1))

s2 = {4,5,6}
print(s2)
print(type(s2))

s3 = set("Hello")
print(s3)

s4 = list(s3)
print(s4)
print("=" * 50)

# 교집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

print("=" * 50)

# 값 1개 추가
s1.add(8)
print(s1)

# 값 여러개
s1.update([43,3,3,5,6,7,3,3,2])
print(s1)

# 값 제거
s1.remove(3)
print(s1)

i = input()
print(i)
