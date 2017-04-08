# 类型判断(一)
print("******************************")


class Student(object):
    # 类属性
    name = 'Student'

    def __init__(self, name):
        self.name = name
        print("self=", self)


s = Student('Bob')
print("s=", s)

# 类属性和对象属性

print(Student.name)
print(s.name)
