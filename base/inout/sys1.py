import sys

# 테스트 방법 python .\sys1.py 1 2 3
# 0번은 파일이름 .\sys1.py
args = sys.argv[1:]
for i in args:
    print(i)