# 如何定一个class

class myclass:
    # 构造
    def __init__(self,age,name) -> None:
        # 成员变量以及类型注解
        self.age:int =age
        self.name:str =name
        print("这是构造函数")
    def __del__(self):
        print("这是析构函数")
    
    def mymethod(self):
        print("这是方法")

    
    