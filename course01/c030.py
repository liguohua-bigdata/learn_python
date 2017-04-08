# 常见类型
import types

print(type(123))
print(type("123"))
print(type(None))
print(type(abs))

# 类型判断(一)
print("******************************")
print(type(123) == type(456))
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))

# 类型判断(二)
print("******************************")


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 使用dir(),获得一个对象的所有属性和方法
print("******************************")

print(dir("abc"))

# len()函数内部，它自动去调用该对象的__len__()方法
print("******************************")
print(len('ABC'))
print('ABC'.__len__())

#
print("******************************")


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))  # 有属性'x'吗？
print(obj.x)
print("******************************")

print(hasattr(obj, 'y'))  # 有属性'y'吗？
setattr(obj, 'y', 19)  # 设置一个属性'y'
print(hasattr(obj, 'y'))  # 有属性'y'吗？
print(obj.y)  # 获取属性'y'

print("******************************")
# getattr(obj, 'z') # 获取属性'z',AttributeError: 'MyObject' object has no attribute 'z'
print(getattr(obj, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404

print("******************************")
print(hasattr(obj, 'power'))  # 有属性'power'吗？
fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn
print(fn)
print(fn() == obj.power())  # 调用fn()与调用obj.power()是一样的
