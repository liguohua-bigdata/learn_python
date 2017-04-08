# 1.创建对象
class Animal(object):
    def run(self):
        print("animal ", self, " run.......")


class Dog(Animal):
    pass


class Cat(Animal):
    def run(self):
        print("cat run !!!!!!")

    def eat(self):
        print("cat eat!!!")


# 创建并使用对象
print("***********************")
a = Dog()
a.run()

# 验证对象的类型
print("***********************")
print(isinstance(a, Animal))
print(isinstance(a, Dog))
print(isinstance(a, Cat))

# 创建并使用对象
print("***********************")
a = Cat()
a.run()
a.eat()

# 验证对象的类型
print("***********************")
print(isinstance(a, Animal))
print(isinstance(a, Dog))
print(isinstance(a, Cat))
