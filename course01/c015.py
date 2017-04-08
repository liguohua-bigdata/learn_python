def test(*other):
    print(other)  # 装成tuple
    print(*other)  # 打散tuple


test(1, 2, 3, 4)
print("********************************")
test([1, 2, 3, 4])
