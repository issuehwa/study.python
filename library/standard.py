import math

# 최대 공약수
a = math.gcd(60, 800, 50)
print(a)

#최소 공배수
a = math.lcm(60, 800, 50)
print(a)

import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초컬릿', '젤리']

result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
print(list(result))

# 순열
b = list(itertools.permutations(['1', '2', '3'], 2))
print(b)

# 조합
b = list(itertools.combinations(['1', '2', '3'], 2))
print(b)


from functools import reduce
c = reduce(lambda x, y: x + y, '1b3d5')
print(c)

num_list = [3, 2, 8, 1, 6, 7]
max_num = reduce(lambda x, y: x if x > y else y, num_list)
print(max_num)  # 8 출력

# 객체 형태 그대로 유지하면서 파일 저장, 불러오기
import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

f = open("D:/study/study.python/test.txt", 'rb')
data = pickle.load(f)
print(data)

import os
d = os.environ
print(d)