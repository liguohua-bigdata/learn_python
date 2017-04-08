l = [1, 3, 5, 4, 2]
print(l)
print(*l)  # 打散list
print("********************************")

t = ("zhagnsan", 18, "shandong")
print(t)
print(*t)  # 打散tuple
print("********************************")

d = {"zhangsan": 20, "lisi": 30}
print(d)
print(*d)  # 打散dictionary的key
print("********************************")

s = set([1, 3, 5, 4, 2])
print(s)
print(*s)  # 打散Set
print("********************************")
