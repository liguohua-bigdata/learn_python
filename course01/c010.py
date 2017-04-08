# 是for...in循环，依次把list中的每个元素迭代出来
print("**********************")
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 用索引遍历list
print("**********************")
for i in range(len(names)):
    print(names[i])

# 是for...in循环，依次把tuple中的每个元素迭代出来
print("**********************")
stu = ("zhagnsan", 18, "shandong")
for f in stu:
    print(f)

# 用索引遍历tuple
print("**********************")
for i in range(len(stu)):
    print(stu[i])
