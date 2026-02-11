#如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间
 

# 1 列表生成器
# 所谓列表生成器，就是简单一句命令生成符合规律的列表的方法

## # list方法生成
mylist:list=list(range(1,10))
for key,value in enumerate(mylist):
    print(key,value)

print("###############")
## 将循环生成的变量放到for之前做运算
mylist=[x*x for x in range(1,10)]   
for key,value in enumerate(mylist):
    print(key,value)
## 进一步的，可以对循环变量进行判断
print("###############")
mylist=[x*x for x in range(1,10) if x%2==0]
for key,value in enumerate(mylist):
    print(key,value)

## 上述列表生成器都是直接生成整个列表，
## 并不是一边用一边生成
mglist=[x*x for x in range(1,10) if x%2==0]# 列表
mygenerator=(x*x for x in range(1,10)if x%2==0)# 生成器
print("生成第一个数字",next(mygenerator))
print("生成第二个数字",next(mygenerator))
print("生成第三个数字",next(mygenerator))

print("生成第四个数字",next(mygenerator))
#print("生成第五个数字",next(mygenerator))# 没有第五个，所以抛出StopIteration

# 生成器是可迭代对象
mygenerator=(x*x for x in range(1,10)if x%2==0)# 生成器
for x in mygenerator:
    print(x)