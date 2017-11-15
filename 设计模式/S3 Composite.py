# 组合-结构化模式3／7，通常用来处理实体之间 of 关系，使得这些实体能够更好地协同工作
"""
意图：
将对象组合成树形结构以表示“部分-整体” of 层次结构。
Composite使得用户对单个对象和组合对象 of 使用具有一致性。 
适用性：
你想表示对象 of 部分-整体层次结构。
你希望用户忽略组合对象与单个对象 of 不同，用户将统一地使用组合结构中 of 所有对象
"""


class Component:
    def __init__(self, strName):
        self.m_strName = strName

    def Addsub(self, com):
        pass

    def Display(self, nDepth):

        pass


class Leaf(Component):
    def Addsub(self, com):
        print("leaf can't add")

    def Display(self, nDepth):
        strtemp = "-" * nDepth
        strtemp = strtemp + self.m_strName
        print(strtemp)


class Composite(Component):
    def __init__(self, strName):
        self.m_strName = strName
        self.c = []

    def Addsub(self, com):
        self.c.append(com)

    def Display(self, nDepth):
        strtemp = "-" * nDepth
        strtemp = strtemp + self.m_strName
        print(strtemp)
        for com in self.c:
            com.Display(nDepth + 2)


if __name__ == "__main__":
    p = Composite("Father1")
    p.Addsub(Leaf("Sub1 of Father1"))
    p.Addsub(Leaf("Sub2 of Father1"))
    p1 = Composite("Father2")
    p1.Addsub(Leaf("Sub1 of Father2"))
    p.Addsub(p1)  # 把Father2归入Father1 of Sub
    p.Display(1)
