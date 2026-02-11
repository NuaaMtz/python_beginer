# 数列的迭代
mylist:list=[1,2,3,4,5]
for i in range(0,mylist.__len__()):
    print(mylist[i])
## 数列带有明显的下标，0～N
# 此外，list可以用迭代生成器进行迭代
from collections.abc import Iterable
print(isinstance(mylist,Iterable))# 可迭代
for value in mylist:# list本身不支持迭代
    print("值=",value)
# 带下标的迭代
for i,value in enumerate(mylist):# 迭代器可以生成索引-元素对
    print("下标：",i,";数值:",value)


# 字典的迭代
# 同时迭代
# python的循环比C循环抽象都高
mydic={'a':'A','b':'B','c':'C'}
for key,value in mydic.items():
    print(key,value)


