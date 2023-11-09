n = '''
   123123
'''
# 주석
"""
asdfasf
"""
a = '%10s' %'hi'
print(a)
print(type(a))


print("=" * 50)

# 소수점 
ㅁ = "%0.4f" % 3.123123123\

print(ㅁ)

b = "I test {0} hahah {1}".format("aa", 123, "dd")
print(b)

# 변수로 포멧팅
c = "hahah {number} aaa {day}".format(number = 123, day="3333")
print(c)

print("=" * 50)

#정렬
a = "{0:<10}".format("hi")
print(a)
a = "{0:>10}".format("hi")
print(a)
a = "{0:^10}".format("hi")
print(a)
a = "{0:=^10}".format("hi")
print(a)

#파이썬 3.6이상 f 포멧팅
name = '홍길동'
age = 36
a = f'나의 이름은 {name}, 내 나이{age + 1} {{ 중괄호 }}'
print(a)