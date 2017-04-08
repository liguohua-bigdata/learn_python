from types import MethodType

print("*********************")


class Student(object):
    pass


s = Student()
print("*********************")
s.name = 'Michael'  # 动态给实例绑定一个属性
print(s.name)

print("*********************")


# 定义一个函数作为实例方法

def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print(s.age)  # 测试结果

# 给一个实例绑定的方法，对另一个实例是不起作用的：
print("*********************")
s2 = Student()  # 创建新的实例


# s2.set_age(25)  # 尝试调用方法,AttributeError: 'Student' object has no attribute 'set_age'

# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)
