# coding:utf-8

# 传入参数是函数
def a(func):
    # 输出传入参数
    print(func)
    # 内联函数
    def inner(*args, **kwargs):
        # 输出传入参数
        print(args)
        # 对传入的函数进行处理
        result = func(*args, **kwargs)
        # 传入函数的结果进行校验
        if result == "ok":
            print("result is %s" % result)
        else:
            print("result is failed:%s" % result)
    # 返回内联函数
    return inner


# 装饰器
@a
def test(name):
    return name

# 调用test函数。test函数带有装饰器进行函数增强
test("ok")
