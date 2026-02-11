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


## 函数作为返回值
def mysum(*args):# 这里*args代表任意长度参数，自动打包为tuple
    sum=0
    for value in args:
        sum=sum+value
    return sum

sum=mysum(1,2,3,4,5)# 调用的时候，马上计算
print(sum)

#如果不希望马上计算呢？
def mylazysum(*args):
    def mysum():
        sum=0
        for value in args:
            sum=sum+value
        return sum
    return mysum

sum=mylazysum(1,2,3,4,5)
print(sum)# 返回的是一个函数
print(sum())# 这才是在调用

sum1=mylazysum(1,2,3,4,5)
print(sum==sum1)# 每次定义都是新的函数而不是原来的