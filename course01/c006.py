# 可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a = 123  # a是整数
print(a)
a = 'ABC'  # a变为字符串
print(a)

# Python提供了ord()和chr()函数，可以把字母和对应的数字相互转换：
print(ord('A'))
print(chr(65))

# Python在后来添加了对Unicode的支持，以Unicode表示的字符串用u'...'表示
print(u'中文')

# 字符串转码
print(u'ABC'.encode('utf-8'))
print(u'中文'.encode('utf-8'))
