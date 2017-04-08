print("*******************")
L = [x * x for x in range(10)]
print(L)

# 一边循环一边计算的机制，称为生成器：generator
print("*******************")
g = (x * x for x in range(5))
print(g)
print(g.__next__())
print(g.__next__())
print(next(g))
print(next(g))
print(next(g))
# 迭代生成器
print("*******************")
g = (x * x for x in range(5))
for e in g:
    print(e)