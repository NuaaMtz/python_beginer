# 字典，在C++中又叫做map
# 好处是使用键-值（key-value）存储，具有极快的查找速度

mylist:list=[80,90,85]

print("列表第一个值=",mylist[0])
## 定义
mydic:dict={"He":80,"Mo":90,"Hong":85}# K-V
## 访问
print(mydic['He'])
print(mydic.get('He'))
## 修改
mydic['He']=98
print("修改后值=",mydic['He'])


## 需要牢记的第一条就是dict的key必须是不可变对象
## 因此dict的key大概只能是：整数、字符串、元组
