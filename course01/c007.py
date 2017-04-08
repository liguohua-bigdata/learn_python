# list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))

# 索引来访问list中每一个位置的元素，记得索引是从0开始的
print(classmates[0])  # 第一个元素
print(classmates[-1])  # 最后一个元素
# print(classmates[10])#越界异常:IndexError: list index out of range


# list是变长集合
classmates.append('Adam')  # 追加元素
print(classmates)

classmates.insert(1, 'Jack')  # 插入到指定位置
print(classmates)

classmates.pop()  # 删除最后一个元素
print(classmates)

classmates.pop(1)  # 删除指定索引上的元素
print(classmates)

classmates[0] = 'Sarah'  # 替换指定索引上的元素
print(classmates)

L = ['Apple', 123, True]  # ist里面的元素的数据类型也可以不同
print(L)


s = ['python', 'java', ['asp', 'php'], 'scheme']#list元素也可以是另一个list
print(s)
print(len(s))