# 排序
# sorted()函数是一个高阶函数
# 用sorted()排序的关键在于实现一个映射函数

mylist:list=[-1,-10,10,-100,200,100]

result=sorted(mylist)# 默认对list排序
print(result)

# 按照绝对值排序
# result:list=sorted(key=abs,mylist)
result:list=sorted(mylist,key=abs)# 要求先传可迭代对象
for value in result:
    print(value)

print(result)

## 字典排序？
from typing import Iterator
mydic:dict={'b':1,'a':2,'c':3}
result:list=sorted(mydic)# 为什么对dict排序，返回list?
# dict本身无序，排序后有序，有序只能是list
# print(type(result))
for key in result:
    print("key=:",key,"value=",mydic[key])
    