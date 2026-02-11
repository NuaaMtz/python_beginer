# python中，function()：function是函数对象，（）是调用函数
def function(a:int):
    print("hello world!")
myfunction=function
myfunction(0)

# 现在，我需要增强这个function,希望在其
# 在调用前后输出某些东西，如果在原来的
# function内部添加代码，那么就会破坏原
# 来的逻辑

# Python 装饰器的核心机制正是：
# 接收一个函数作为输入，定义一个新的包装函数（或修改原函数），
# 然后返回这个新函数

# 带参数的修饰器
def mydecorator(function):
    def mydecoratorfunction(b:int):  # 一般来说
        function(2)
        print("TianzhuMo")
    return mydecoratorfunction
function1=mydecorator(function)
function1(1)

# 带参数的装饰器使用@语法
@mydecorator
def function2(a:int):
    print("TianzhuMo2")
function2(2)