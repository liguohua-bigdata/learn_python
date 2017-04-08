class Student(object):
    name = 'Student'


s = Student()  # 创建实例s

print(Student.name)  # 打印类的name属性
print(s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性

print("*********************")
s.name = 'Michael'  # 给实例绑定name属性

print(Student.name)  # 打印类的name属性
print(s.name)  # 打印name属性

print("*********************")
del s.name  # 如果删除实例的name属性
print(Student.name)  # 打印类的name属性
print(s.name)  # 打印name属性


# 不要把实例属性和类属性使用相同的名字
