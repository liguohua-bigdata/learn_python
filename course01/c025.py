# 直接使用匿名函数
l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)

# 匿名函数也可以赋值到变量
f = lambda x: x * x
l = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)

print("*******************")


# 匿名函数做返回值
def add_lazy(x, y):
    return lambda: x + y


f = add_lazy(3, 2)
print(f)  # 函数本身
print(f())  # 函数调用


# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
