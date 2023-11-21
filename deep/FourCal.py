class FourCal:
  # 생성자
  def __init__(self, first, second):
    self.first = first
    self.second = second

  def setdata(self, first, second):
    self.first = first
    self.second = second
  def add(self):
    result = self.first + self.second
    return result
  def mul(self):
    result = self.first * self.second
    return result
  def sub(self):
    result = self.first - self.second
    return result
  def div(self):
    result = self.first / self.second
    return result
  pass


# a = FourCal(5,3)

# a.setdata(4,2)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())

# 상속
class MoreFourCal(FourCal):
  def pow(self):
    result = self.first ** self.second
    return result

# 오버 라이딩
class SafeFourCal(FourCal):
  def div(self):
    if (self.second == 0):
      return 0
    else:
      return self.first / self.second

a = MoreFourCal(2,3)
print(a.add())
print(a.pow())

b = SafeFourCal(4, 0)
print(b.div())