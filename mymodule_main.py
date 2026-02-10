# 一个module代表一个py文件，而不是一个类或者一个函数
# 引入全部
import  mymodule 
mymodule.myprint(1)

from mymodule import *
myprint(3)

# 引入一个函数
from mymodule import myprint
myprint(2)

