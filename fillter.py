# fillter
# 和map,reduce语法接近
# 但是它输入的函数要求返回是bool
# 返回值是去掉False元素后的列表

def checkis2(a:int):
    if a==2:
        return True
    else:
        return False
    
mylist:list=[x for x in range(-10,10)]

from typing import Iterator
result:Iterator=filter(checkis2,mylist)
for i,value in enumerate(result):
    print(i,value)
