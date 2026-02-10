# 取一个list[]或tuple()的部分元素


## 创建一个list

mylist=[]
for i in range(0,10000):
    mylist.append(i+1)

## 切片
print(mylist[0:100])# 取前100个参数
print("切片从0开始的时候可以省略",mylist[:100])# 取前100个参数,[)

# 负数是从最后一个元素-1往前减1去访问
# 但是切片的方法还是与正数一样
print("取出倒数第二个",mylist[-2:-1])
print("取出倒数第二个",mylist[-2:])
# 字符串是特殊的list

print('12345'[1:2])

