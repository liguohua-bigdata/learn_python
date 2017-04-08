#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self):
        self.name = 'Michael'

    # 只有在没有找到属性的情况下，才调用__getattr__
    def __getattr__(self, attr):
        if attr == 'score':
            return 99


s = Student()
print(s.name)
print(s.score)
