# 쓰기 w 모드
f = open("새파일.txt", "w", encoding='UTF-8')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 추가하기 a모드
f = open("D:/study/study.python/새파일.txt", "a", encoding='UTF-8')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 읽기 r 모드
f = open("D:/study/study.python/새파일.txt", 'r', encoding='UTF-8')

lines = f.readlines()
for line in lines:
    print(line)
f.close()

# lines = f.readlines()
# for line in lines:
#     line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
#     print(line)
# f.close()

# with 문
# 지역변수 화
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")