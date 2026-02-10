from myclasss import myclass 

class SonOfMyClasss(myclass):
    def __init__(self):
        self.publicX=10
        self.__privateX=20# 下划线代表private
        self._protectedX=40# protected,不能被import *  
        print("这是子类的构造")

    def __del__(self):
        self._privateX=30
        print("这是子类的析构")

    def mymethod(self):
       
        print("这是子类方法")