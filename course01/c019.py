from collections import Iterable

# 字典迭代
print("*******************")
d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
    print(k, "->", d[k])

# 字典迭代2
print("*******************")
d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, "->", v)

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
print(isinstance('123', Iterable))

print("*******************")
print(isinstance(123, Iterable))

print("*******************")
print(isinstance([1, 2, 3], Iterable))

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对
print("*******************")
L = ['A', 'B', 'C']
for i, v in enumerate(L):
    print(i, "->", v)

# for循环里，同时引用了两个变量，在Python里是很常见的
print("*******************")
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, ",", y)
