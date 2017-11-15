# 根据函数名称动态调用


def do_foo():
    print("执行了函数do_foo!")


def do_bar():
    print("执行了函数do_bar!")


class myClass():
    def do_foo(self):
        print("执行foo!")

    def do_bar(self):
        print("执行bar!")

    @staticmethod
    def static_foo():
        print("执行static foo!")

    @staticmethod
    def static_bar():
        print("执行static bar!")


def main():

    obj = myClass()

    func_name = "do_foo"
    static_name = "static_foo"

    print("1.")
    eval(func_name)() #字符串转到函数名称并执行
    print("2.")
    getattr(obj, func_name)() #从一个class中查询是否存在指定名称到函数，并执行
    print("3.")
    getattr(myClass, static_name)()

    func_name = "do_bar"
    static_name = "static_bar"

    print("4.")
    eval(func_name)()
    print("5.")
    getattr(obj, func_name)()
    print("6.")
    getattr(myClass, static_name)()


if __name__ == '__main__':
    main()
