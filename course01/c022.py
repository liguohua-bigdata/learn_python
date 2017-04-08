from collections import Iterable
from typing import Iterator

# list
print("*************************")
v = isinstance([], Iterable)
print(v)
# dict
print("*************************")
v = isinstance({}, Iterable)
print(v)
# string
print("*************************")
v = isinstance('abc', Iterable)
print(v)
# 生成器,生成器都是Iterator对象
print("*************************")
g = (x for x in range(10))
v = isinstance(g, Iterable)
print(v)

# list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print("*************************")
v = isinstance(iter([]), Iterator)
print(v)
print("*************************")
v = isinstance(iter({}), Iterator)
print(v)
print("*************************")
v = isinstance(iter(()), Iterator)
print(v)
print("*************************")
v = isinstance(iter('abc'), Iterator)
print(v)

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
