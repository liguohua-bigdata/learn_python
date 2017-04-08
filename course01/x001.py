class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def say(self):
        print(self.__name,"->", self.__age)


s1 = Student("xiao zhang", 13)
s1.say()
s2 = Student("xiao li", 15)
s2.say()

