# 实现一个 @timer 装饰器，记录函数的运行时间，
# 注意需要考虑函数可能会接收不定长参数。
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        running_time = end - start
        print(f"{func.__name__} running_time: {running_time}")
        return res
    return decorated



@timer
def sleep1(n):
    print(f'sleep1 start')
    time.sleep(n)
    print(f'sleep1 end')

@timer
def sleep2(*args, **kwargs):
    print(f'sleep2 start')
    print(f"args: {args}")
    print(f'kwargs: {kwargs}')
    time.sleep(len(args) + len(kwargs))
    print(f'sleep2 end')

if __name__ == "__main__":
    sleep1(1)
    sleep2(1, 2, age=20)