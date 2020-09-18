# 自定义一个 python 函数，实现 map() 函数的功能。
def my_map(func, iterables):
    return (func(i) for i in iterables)


if __name__ == "__main__":
    print(list(my_map(lambda x: x*2, [1, 2, 3])))
