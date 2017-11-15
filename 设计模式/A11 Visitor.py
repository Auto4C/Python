# 访问者
'''
意图：
封装了对象结构元素之上的操作，使得新增元素的操作变得非常简单。
对象结构存储了不同类型的元素对象，以供不同访问者访问
适用性：
对象结构中对象对应的类很少改变，但经常需要在此对象结构上定义新的操作。
需要对一个对象结构中的对象进行很多不同的并且不相关的操作，而需要避免让这些操作“污染”这些对象的类，也不希望在增加新操作时修改这些类
'''


class Node(object):
    pass


class A(Node):
    pass


class B(Node):
    pass


class C(A, B):
    pass


class Visitor(object):
    def visit(self, node, *args, **kwargs):
        meth = None
        for cls in node.__class__.__mro__:
            meth_name = 'visit_' + cls.__name__
            meth = getattr(self, meth_name, None)
            if meth:
                break

        if not meth:
            meth = self.generic_visit
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print('generic_visit ' + node.__class__.__name__)

    def visit_B(self, node, *args, **kwargs):
        print('visit_B ' + node.__class__.__name__)


a = A()
b = B()
c = C()
visitor = Visitor()
visitor.visit(a)
visitor.visit(b)
visitor.visit(c)
