# if语句
print("*******************")
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

# if-esle语句
print("*******************")
age = 12
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenage')

# if-elif-esle语句
print("*******************")
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
print("*******************")
x = 1
if x:
    print('True')
print("*******************")
x = "a"
if x:
    print('True')
print("*******************")
x = ""
if x:
    print('True')
