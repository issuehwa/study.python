# 예외처리
try :
  4/ 0
except BaseException as e:
  print(e)

finally:
  print('파이널리~')

# 여러개 에러
try :
  a = [1, 2]
  print(a[2])
  4/ 0
except ZeroDivisionError:
  print('0으로 나눌 수 없습니다.')

except IndexError:
  print('인덱싱 할 수 없습니다.')

except (TypeError, NameError) as e:
  print(e)

finally:
  print('파이널리~2')


# try-eles 문
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

# 오류 회피
try:
  f = open("나없는파일", 'r')
except FileNotFoundError:
  pass


# 오류 발생 raise
# class Bird:
#     def fly(self):
#         raise NotImplementedError

# class Eagle(Bird):
#     pass

# eagle = Eagle()
# eagle.fly()

# # 커스텀 예외 만들기
# class MyError(Exception):
#     def __str__(self):
#         return "허용되지 않는 별명입니다."
