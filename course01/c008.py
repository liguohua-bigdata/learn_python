# tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# 元组也有索引
print(classmates[0])
print(classmates[-1])

# 元组也有长度
print(len(classmates))

# 元组不能修改:'tuple' object does not support item assignment
# classmates[0]="zhangsan"

# 空的tuple
t = ()
print(t)
# 有一个元素的tuple
t = (1)
print(t)
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)

# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
t = ('a', 'b', ['A', 'B'])
print("改变前:",t)
t[2][0] = 'X'
t[2][1] = 'Y'
print("改变后:",t)