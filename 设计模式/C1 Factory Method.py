#工厂方法-创建模式1／5，提供实例化的方法，为适合的状况提供相应的对象创建方法
'''
###意图：
定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method使一个类的实例化延迟到其子类。
###适用性：
当一个类不知道它所必须创建的对象的类的时候。
当一个类希望由它的子类来指定它所创建的对象的时候。
当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候。
'''


class ChinaGetter:
    """翻译成中文的实现类"""

    def __init__(self):
        self.trans = dict(dog=u"小狗", cat=u"小猫")

    def get(self, msgid):
        """翻译动作get"""
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)


class EnglishGetter:
    """翻译成英文的实现类"""

    def get(self, msgid):
        return str(msgid)

class JapanGetter:
    """该实现动作留待后续添加修改"""

    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    """工厂模式：定义了接口def get_localizer，罗列所有支持语言，但没有做相关翻译但动作"""
    languages = dict(English=EnglishGetter, China=ChinaGetter,Japan=JapanGetter)
    return languages[language]()


# Create our localizers
ToEN, ToCN = get_localizer("English"), get_localizer("China")
# Localize some text
for msgstr in "dog parrot cat bear".split():
    print(ToEN.get(msgstr),"-->", ToCN.get(msgstr))