L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 从索引0开始取，直到索引3为止，但不包括索引3
print(L[0:3])
print(L[:3])
# 从倒数第二个切
print(L[-2:])

L = list(range(100))
# 每5个取一次
print(L[::5])
# 复制原来的List
print(L[:])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
T = (0, 1, 2, 3, 4, 5)
print(T[:3])

# 字符串'xxx'也可以看成是一种list
S = "ABCDEFG"
print(S[:3])
