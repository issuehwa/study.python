from module_test import mod1, mod2
import sys
# 절대경로로만
sys.path.append("d:/study/study.python/deep")
import mod3

print(mod1.add(4, 5))

a = mod2.Math()
print(a.solv(3))


print(mod3.name)