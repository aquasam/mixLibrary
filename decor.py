# -*- coding:utf8 -*-
# Author : Samuel

'''
    装饰器语法
        装饰器
        可传参装饰器
        带参装饰器
        装饰器返回值
'''
#装饰器
def decor(func):
    def wrapper():
        print("装饰函数前面部分")
        func()
        print("装饰函数后面部分")
    return wrapper

#装饰器使用
@decor
def decorTest():
    print("被装饰函数内部")

'''----------------------------------------------------------------'''


#可传参装饰器
def decor1(func):
    def wrapper(name):
        print("装饰函数前面部分")
        print("装饰器内输出参数：{}".format(name))
        func(name)
        print("装饰函数后面部分")
    return wrapper

#带参装饰器使用
@decor1
def decorTest1(name):
    print("被装饰函数内输出参数：{}".format(name))

'''----------------------------------------------------------------'''


#带参装饰器
def decor2(cond):
    def external(func):
        def wrapper():
            print("装饰器传入参数:{}".format(cond))
            print("装饰函数前面部分")
            func()
            print("装饰函数后面部分")
        return wrapper
    return external

#带参装饰器使用
@decor2(cond = "装饰器参数")
def decorTest2():
    print("被装饰函数内")



'''----------------------------------------------------------------'''

#装饰器返回值

def decor3(func):
    def wrapper(name):
        print("装饰函数前面部分")
        print("装饰器内输出参数：{}".format(name))
        funcname = func(name)
        print("装饰函数后面部分")
        return funcname
    return wrapper

#装饰器返回值使用
@decor3
def decorTest3(name):
    return name




'''----------------------------------------------------------------'''



if __name__ == "__main__":
    # decorTest()

    decorTest1(name="参数1")
    # decorTest2()
    # print("传出参数：{}".format(decorTest3("参数")))