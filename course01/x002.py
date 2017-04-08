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


print("***********************")
a = Dog()
a.run()

print("***********************")
print(isinstance(a, Animal))
print(isinstance(a, Dog))
print(isinstance(a, Cat))

print("***********************")
a = Cat()
a.run()
a.eat()

print("***********************")
print(isinstance(a, Animal))
print(isinstance(a, Dog))
print(isinstance(a, Cat))
