# 高阶函数
# 所谓高阶函数，就是函数作为变量使用

# 1. 函数指向变量

def myfunction(a:int):
    print('Hello World!','数字为=',a)
## 普通调用函数
myfunction(1)
## 函数作为变量，相当于给函数别名
myfuction2=myfunction
myfuction2(2)


#一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数

def myhigherorder(myfunction,a):
    myfunction(a)

myhigherorder(myfunction=myfunction,a=3)
