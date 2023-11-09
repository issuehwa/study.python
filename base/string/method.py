# 문자열 메소드
a = "hooby"
print(a.count('b'))


# 없는 글자 -1
print(a.find('b'))
print(a.find('x'))

# 없는 글자 찾을 시 오류
# print(a.index('a'))

print("=" * 50)

# 문자열 사이에 삽입
a = ", ".join("abcd")
print(a)


print("=" * 50)

# 공백 지우기
a = "  hi  "
print(a.lstrip()) #왼쪽 공백
print(a.rstrip()) #오른쪽 공백
print(a.strip()) #양쪽 공백

print("=" * 50)

# 문자열 바꾸기
a = "Life   is    to o short"
print(a.replace("Life", "Your leg"))

# 나누기
print(a.split())