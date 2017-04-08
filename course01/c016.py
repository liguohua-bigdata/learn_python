def test(**kwargs):
    print(kwargs)  # 装成dictionary

    print(*kwargs)  # 打散dictionary的key

    keys = kwargs.keys()
    for k in keys:
        print(k, "->", kwargs[k])


test(name="zhagnsan", age=15)

# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
