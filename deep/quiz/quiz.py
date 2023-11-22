# result = 0
# for n in range(1, 1000):
#     if n % 3 == 0 or n % 5 == 0: 
#         result += n
# print(result)

# result = 0
# a, b, c = 1, 1, 0
# while c < 4_000_000:
#   c = a + b
#   a = b
#   b = c
#   if c % 2 == 0: result += c

# print(result)

# def factorization(x):
#     d = 2
#     result = 0

#     while d <= x:
#         if x % d == 0:
#             result = d
#             x = x / d
#         else:
#             d = d + 1

#     return result

# a = factorization(600851475143)
# print(a)

# from decimal import *
# getcontext().prec = 100   #소수점이하 100자리까지 설정.

# for d in range(2, 1000) :
#   a = Decimal(1)/Decimal(d)
#   print(a)

# def func(*a, **b):
#     print(a)

# func(1, 2, 3, name='foo', age=3)


# a: int = 1

# a= '2'
# print(a)

# def add(a:int, b:int) -> int:
#   return a+b

data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))