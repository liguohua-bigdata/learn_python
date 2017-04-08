def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)  # 函数本身
print(f())  # 函数调用

v = lazy_sum(1, 3, 5, 7, 9)()  # 函数调用,返回数值
print(v)
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
print("*******************")
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)
print("*******************")
v1 = lazy_sum(1, 3, 5, 7, 9)()
v2 = lazy_sum(1, 3, 5, 7, 9)()
print(v1 == v2)
# 函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

fs = count()#返回包含三个函数的list
print(fs)

print("*******************")
# 分别查看这三个lazy函数,此时函数并没有执行
f0=fs[0]
print(f0)
f1=fs[1]
print(f1)
f2=fs[2]
print(f2)

#分别执行者这三个lazy函数,此时i=3,所以
print("*******************")
print(f0())
print(f1())
print(f2())
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。