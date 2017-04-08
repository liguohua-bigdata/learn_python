# 这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value
print("*********************************")
dic = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
for k in dic:
    print(k, "->", dic[k])

# 追加数据
print("*********************************")
dic['Adam'] = 67
print(dic)

# 更改数据
print("*********************************")
dic['Adam'] = 190
print(dic)

# 删除数据
print("*********************************")
dic.pop('Adam')
print(dic)

# 获取数据
print("*********************************")
k = 'Bob'
v = dic.get(k)
print(k, "->", v)

# 避免报错,获取数据
print("*********************************")
k = 'Bob'
if k in dic:
    v = dic.get(k)
    print(k, "->", v)
else:
    print(k + "is not in dictionary!")

# dict内部存放的顺序和key放入的顺序是没有关系的。
# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而增加；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
# dict的key必须是不可变对象。
