# 如果一个函数在内部调用自身本身，这个函数就是递归函数。
# 使用递归函数需要注意防止栈溢出
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(50))