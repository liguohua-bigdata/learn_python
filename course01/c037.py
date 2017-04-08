#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name

    # toString()方法
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # debug版的toString()方法
    __repr__ = __str__


s = Student('Michael')
print(s)
