treeHit = 0
while treeHit < 10:
  treeHit = treeHit +1
  print("나무를 %d번 찍었습니다." % treeHit)
  if treeHit == 10:
    print("나무 넘어갑니다.")



# for 문
for i in range(2,10):        # 1번 for문
    for j in range(1, 10):   # 2번 for문
        print(i*j, end=" ")  # print(i*j, end="\n") 디폴드값 줄바꿈
    print('') 


# 비주얼 스튜디오 코드 디버그

# 리스트 컴프리헤션 list comprehension

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

result = [num * 3 for num in a]
print(result)

# 결과 / 반복 / 조건
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# 이중 포문
result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)