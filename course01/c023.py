# map,元素乘方
from functools import reduce
from locale import normalize

print("*************************")


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4])  # 返回一个Iterator,Iterator是惰性序列
l = list(r)
print(l)

# map,将元素转换为字符串
print("*************************")
l = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)

# reduce,计算累加和
print("*************************")


def add(x, y):
    return x + y


r = reduce(add, [1, 2, 3, 4, 5])
print(r)

# filter,过滤出偶数
print("*************************")


def is_odd(n):
    return n % 2 == 0


l = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(l)

# sorted,按绝对值排序
print("*************************")
l = sorted([36, 5, -12, 9, -21], key=abs)  # sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(l)


l = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(l)

l = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
print(l)