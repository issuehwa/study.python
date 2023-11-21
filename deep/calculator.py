result = 0

def add(num):
    global result
    result += num  # 결괏값(result)에 입력값(num) 더하기
    return result  # 결괏값 리턴

print(add(3))
print(add(4))

# 클래스
# self 가 this
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()


print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))