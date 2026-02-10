from myclasss import myclass 
# 自动运行构造和析构
a=myclass(age=23,name="Tianzhu Mo")

from class_inheritance import SonOfMyClasss
# 父类构造->子类构造
# 父类析构->子类析构
a=SonOfMyClasss()
# a.age# 子类没有给父类传递
# a.__privateX# 双下划线无法被类外访问
a.publicX
a._protectedX
a.mymethod()