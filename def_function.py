# c++中函数传递包括值传递和引用传递
# 在python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。


# 不可变类型包括： 整数、字符串、元组
# 相当于值传递而非引用传递
def fun1(a):
    # 此时传进来的a是b复制而来的
    # 即使修改了a也不会影响b
    a=2
    return a
b=1
print(fun1(b),b)

#可变类型包括：列表，字典

def fun2(a:list):
        a.clear()
        # 此时修改a等于修改b
        a.append(10)
        a.append(20)
        a.append(30)
        return a
b=[1,2,3]
print(fun2(b),b)


# 自定义类型也是可变类型
# 可变类型相当于引用类型
# 创建新对象相当于创建新引用

# 自定义类型
class mytype:
      def __init__(self,a) ->None:
            self.x=a
def fun3(a:mytype):
      a.x=300
      return a
a=100
a=mytype(a)
print(a.x)
b=fun3(a)
print(a.x,b.x)# a传进去，且被修改 

def fun4(a:mytype):
      a=mytype(200)
      return a

b=fun4(a)
print(a.x,b.x)# a传进去，但是没有被修改