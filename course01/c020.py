# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
import os

print("*******************")
l = list(range(1, 11))
print(l)
# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
print("*******************")
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

print("*******************")
L = [x * x for x in range(1, 11)]
print(L)

# for循环后面还可以加上if判断
print("*******************")
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

# 还可以使用两层循环，可以生成全排列：
print("*******************")
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
print("*******************")
L = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
print(L)

# 列表生成式也可以使用两个变量来生成list：
print("*******************")
d = {'x': 'A', 'y': 'B', 'z': 'C'}
l = [k + '=' + v for k, v in d.items()]
print(l)

# 把一个list中所有的字符串变成小写
print("*******************")
L = ['Hello', 'World', 'IBM', 'Apple']
L = [s.lower() for s in L]
print(L)
