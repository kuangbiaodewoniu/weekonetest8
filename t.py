# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: t.py 
@time: 2018/03/19 
"""
from datetime import datetime
# 装饰器


def log(func):

    def decorator(*args, **kwargs):
        print(func.__name__+' has been called at '+datetime.now().strftime('%y-%m-%d %H:%M:%S'))
        return func(*args, **kwargs)
    return decorator


@log
def add(x, y):
    return x + y


# 可迭代是指可以用for in ,迭代器指可迭代对象其实是实现了 __iter__ 和 __next__ 这俩个魔法方法

# 字典解析
dic = {'a': 1, 'b': 2, 'c': 3}
new_dic = {k: v*v for k, v in dic.items()}

# 列表解析
numbers = [1,2,3,4,5,6]
new_numbers = [index*index for index in numbers if index % 2 == 0]

# 切片
letters = ['a', 'b', 'c', 'd', 'e']
new_letters = letters[:-1]

# 匿名函数
double = lambda x: x*x

if __name__ == '__main__':
    result = double(10)
    print(result)
    print(new_letters)
    print(new_numbers)
    print(new_dic)
    add(11, 12)