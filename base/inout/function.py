def add(a, b):
  return a + b

print(add(3, 5))

def say(): return 'hi'

print(say())
print("=" * 50)

def add_many(*args):
  result = 0
  for i in args:
    result = result + i
  return result

print(add_many(12,3,3,4,5,6,76,7,8,2))
print("=" * 50)

# 딕셔너리 (맵) 형태로 받는다
def print_kwargs(**kwargs):
  print(kwargs)

print_kwargs(a=1, b=2)

print("=" * 50)
# scope

a = 1
def vartest(a):
    a = a +1
    print(a)

vartest(a)
print(a)

print("=" * 50)
# 글로벌
# vartest_global.py
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)

# lamdbda
add = lambda a, b: a+b
print(add(3,5))