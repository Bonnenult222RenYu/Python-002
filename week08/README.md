# 作业

## 作业一

+ list
  + 容器序列，可变
+ tuple
  + 容器序列，不可变
+ str
  + 扁平序列，不可变
+ dict
  + 容器序列，可变
+ collections.deque
  + 容器序列，可变



## 作业二

```python
# 自定义一个 python 函数，实现 map() 函数的功能。
def my_map(func, iterables):
    return (func(i) for i in iterables)


if __name__ == "__main__":
    print(list(my_map(lambda x: x*2, [1, 2, 3])))
# [2, 4, 6]
```



## 作业三

```python
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
'''
sleep1 start
sleep1 end
sleep1 running_time: 1.0001842975616455
sleep2 start
args: (1, 2)
kwargs: {'age': 20}
sleep2 end
sleep2 running_time: 3.000331401824951 
'''
```

