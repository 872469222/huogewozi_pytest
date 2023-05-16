
'''
模块级（setup_moudle/teardown_moudule ）模块始末，全局的（优先最高）
函数级（setup_class/teardown_class）只对函数用例生效（不在类中）
类级（setup_function/teardown_function）只在类中前后运行一次（在类中）
方法级（setup_method/teardown_method ）开始于方法始末（在类中）
类里面的（setup/teardown）运行在调用方法的前后
'''
# ceshissaaaa
# 模块级别,只被调用一次
def setup_module():
    print("资源准备:setup module")

def teardow_module():
    print("资源准备：teardown module")

def test_case1():
    print("case1")

def test_case2():
    print("case2")

def setup_function():
    print("资源准备：setup function")

def teardown_function():
    print("资源销毁: teardown function")

class TestDemo1:

# 执行类 前后分别执行setup_class teardown_class
        def setup_class(self):
            print("TestDemo setup_class")

        def teardown_class(self):
            print("TestDemo teardown_class")

# 每个类里面的方法前后分别执行setup,teardown
        def setup(self):
            print("TestDemo setup")

        def teardown(self):
            print("TestDemo teardwon")

        def test_demo1(self):
            print("test demo1")

        def test_demo2(self):
            print("test demo2")
class demo1:
#执行类 前后分别执行setup_class teardown_class
        def setup_class(self):
            print("TestDemo setup_class")

