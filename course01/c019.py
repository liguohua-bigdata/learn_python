# 字典迭代
from collections import Iterable

print("*******************")
d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
    print(k, "->", d[k])

# list迭代
print("*******************")
l = [1, 3, 2, 4, 5]
for e in l:
    print(e)

# tuple迭代
print("*******************")
t = ("zhagnsan", 18, "female")
for f in t:
    print(f)

# 字符串迭代
print("*******************")
s = "abcdefg"
for e in s:
    print(e)
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print("*******************")
print(isinstance('abc', Iterable))
