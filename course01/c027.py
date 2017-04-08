import functools

v = int('12345')
print(v)

v = int('12345', base=8)
print(v)
# 自定义函数
print("***************")


def int8(x, base=8):
    return int(x, base)


v = int8('12345')
print(v)

# 使用偏函数
print("***************")
int8 = functools.partial(int, base=8)
v = int8('12345')
print(int8)
print(v)
