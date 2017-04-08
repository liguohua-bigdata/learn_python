# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print('2015-3-25')


f = now  # 将函数赋值给变量
print(f)
print(now)
print(f == now)
# 函数对象有一个__name__属性，可以拿到函数的名字：
print("*******************")
print(f.__name__)
print(now.__name__)
print(f.__name__ == now.__name__)



# decorator就是一个返回函数的高阶函数
print("*******************")
# 1.定义装饰器
def log(func):
    def wrapper(*args, **kw):
        print('这里是代码增强')
        return func(*args, **kw)
    return wrapper
# 2.在定义函数的时候使用装饰器,把@log放到now()函数的定义处,相当于执行now = log(now)
@log
def now2():
    print('2015-3-25')
# 3.函数调用,先调用装饰器,然后调用函数本身
now2()

# 把@log放到now()函数的定义处,相当于执行now = log(now)
print("*******************")
def now3():
    print('2015-3-25')
now3=log(now3)
now3()


print("*******************")
print("*******************")
print("*******************")
print("*******************")

# 一个更复杂的例子
# 1.定义带参装饰器
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('传输的参数是: %s, 调用的方法是: %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
# 2.使用带参装饰器
@log('execute')
def now():
    print('2015-3-25')
# 3.验证带参装饰器
now()


print("!!!!*******************")
print(log('execute'))# decorator函数
print("!!!!*******************")
print(log('execute')(now))# wrapper函数
print("!!!!*******************")
print(log('execute')(now)())# 调用wrapper函数
