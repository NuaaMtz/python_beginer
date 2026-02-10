# 函数传参顺序

def fun1(a):
    a=10
    return a 
print(fun1(1))

# 关键字参数
# =None意味着可以缺省
def fun2(name,age=1,other=None):
    print("name=",name)
    print("age=",age)
    print("other=",other)

fun2(age=10,name='Tianzhu Mo')
fun2(age=10,name='Tianzhu Mo',other="无")




    