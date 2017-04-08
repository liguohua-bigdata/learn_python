#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
    @property
    def age(self):
        return 2015 - self._birth

s = Student()
s.birth=123
print(s.birth)
print(s.age)
