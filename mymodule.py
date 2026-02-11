# module的定义方法

def myprint(par):
    print("Hello World!") 


# 在Python中，一个.py文件就称之为一个模块（Module）



# mycompany                <----1.顶层包名
#  ├─ web                    <----2. 次层包名
#  │  ├─ __init__.py      <----3. 每个包都需要有一个__init__.py
#  │  ├─ utils.py            <----4. 模块1
#  │  └─ www.py
#  ├─ __init__.py
#  ├─ abc.py               <----5. 模块N
#  └─ utils.py

