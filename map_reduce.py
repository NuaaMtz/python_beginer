# map相当于将list里面的数字带入函数得到结果
mylist:list=[1,2,3,4,5]
def add(a:int):
        return a+1

from typing import Iterator
result:Iterator[int]=map(add,mylist)# 返回迭代器
for value in result:
        print(value)

# reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
## 感觉没多大用，就是要求函数输入两个参数，每次函数的值都被作为下一次迭代的第一个参数