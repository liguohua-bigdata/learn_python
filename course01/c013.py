# 函数调用
from filecmp import cmp

print("*********************************")
print(abs(-12))
print("*********************************")
print(cmp(1, 2))

print("*********************************")
v = int('123') + int("234")
print(v)

print("*********************************")


# 函数定义
def test():
    print("hello world python!")


# 函数调用
test()

print("*********************************")


# 函数定义
def test(name):
    print("hello world python! " + name)


# 函数调用
test("zhangsan")

print("*********************************")


# 函数定义
def add(a, b):
    return a + b


# 函数调用
print(add(123, 234))

print("*********************************")


# 函数定义,默认参数,默认参数必须指向不变对象！
def mut(a, b=200):
    return a * b


# 函数调用
print(mut(2))
print(mut(2,15))
print("*********************************")


# 函数定义,可变参数,可变参数就是一个tuple
def add2(a,b,*other):
   s=a+b
   for o in other:
       s+=o
   return s

# 函数调用
print(add2(2,3))
print(add2(2,15,4,5,6,7,8,9))
print("*********************************")

# 函数定义,空函数
def nop():
    pass
