# ******************************************************************************
# APIBinder:API绑定器，用于提供运行时API绑定服务。
# ******************************************************************************
import random


class APIBinder:
    def PlugChip(self, controller):
        pass
# *******************************************************************************
# BindUnit:参与API绑定的所有类的基类。
# *******************************************************************************


class BindUnit:
    pass
# *******************************************************************************
# Event Center: Event交换中心，提供运行时动态dispatch各种event的服务。
# *******************************************************************************


class EventCenter:
    pass
# *******************************************************************************
# EventUnit: 参与Event收发的所有类的基类。
# *******************************************************************************


class EventUnit:
    pass
# *******************************************************************************
# Controller类是本例子中的核心应用逻辑所在类。
# 它将利用Computer类提供的算术计算API进行算术运算，并以data_in事件的形式向
# Processor类发送计算结果。
# *******************************************************************************


class Controller(BindUnit, EventUnit):
    def __init__(self, name):
        BindUnit.__init__(self, name)
        EventUnit.__init__(self, name)

    # 私有方法，由于响应tick事件，实施主要的应用逻辑。
    def __DoControl(self):
        # 注：此处出现的Call()方法是基类BindUnit提供的。下同。
        x = self.Call('comp_rand', 100)  # 调用外部API生成随机数
        y = self.Call('comp_rand', 100)  # 调用外部API生成随机数

        print("--------------------------------------")
        # *******************************
        # 作加法运算
        # *******************************
        result = self.Call('comp_add', x, y)  # 调用外部API运算
        message = "%d + %d = %d" % (x, y, result)

        # 注：此处出现的SendEvent()方法是基类EventUnit提供的。下同。
        self.SendEvent('data_in', message)  # 以事件形式发送运算结果。

        # *******************************
        # 作减法运算
        # *******************************
        result = self.Call('comp_minus', x, y)  # 调用外部API运算
        message = "%d - %d = %d" % (x, y, result)

        self.SendEvent('data_in', message)  # 以事件形式发送运算结果。

        # *******************************
        # 作乘方运算
        # *******************************
        result = self.Call('comp_power', x)  # 调用外部API运算
        message = "%d * %d = %d" % (x, x, result)

        self.SendEvent('data_in', message)  # 以事件形式发送运算结果。

        print("--------------------------------------/n")

    # 继承自BindUnit的方法。将被APIBinder调用。
    # 返回需要的API列表表格给APIBinder，由APIBinder来填表以完成绑定。
    # 完成绑定后，API映射表中的None将变为可调用的方法地址。
    # 大白话：嘿，Binder，我需要这些API，请替我绑定吧。
    def _getDependingAPI(self):
        return {'comp_add': None, 'comp_minus': None, 'comp_power': None,
                'comp_rand': None}
    # 继承自EventUnit的方法。将被EventCenter调用。
    # 返回自己订阅的事件映射表，包括事件名称和对应的handler。
    # 大白话：嘿，EventCenter，我订阅这些Event，如果有人产生，请一定给我。

    def _getEventDispatcher(self):
        return {'tick': self.__DoControl}

# *******************************************************************************
# Computer类提供基本算术API供其他模块使用.
# *******************************************************************************


class Computer(BindUnit):
    def __init__(self, name):
        BindUnit.__init__(self, name)

    # 继承自BindUnit的方法。将被APIBinder调用。
    # 返回提供的API列表表格给Binder，由APIBinder用于API绑定。
    # API映射表中记录了API的名称和自己类方法的入口地址。
    # 大白话：嘿，Binder，我提供这些API，拿去给需要的人用吧。
    def _getDependedAPI(self):
        return {'comp_add': self.__Add, 'comp_minus': self.__Minus,
                'comp_power': self.__Power,
                'comp_rand': self.__MakeRandom}
    # 加运算API，私有方法，仅向Binder公开。

    def __Add(self, x, y):
        return x + y

    # 减运算API，私有方法，仅向Binder公开。
    def __Minus(self, x, y):
        return x - y

    # 幂运算API，私有方法，仅向Binder公开。
    def __Power(self, x):
        return x * x

    # 生成随机数的API，私有方法，仅向Binder公开。
    def __MakeRandom(self, scope):
        x = random.randint(0, scope)
        return x


# ***************************************************************************
# Processor类接收名为data_in的事件来处理来自Controller的计算结果信息.
# ***************************************************************************
class Processor(EventUnit):
    def __init__(self, name):
        EventUnit.__init__(self, name)

    # 继承自EventUnit的方法。将被EventCenter调用。
    # 返回自己订阅的事件映射表，包括事件名称和对应的handler。
    # EventCenter将根据这里的订阅条目决定运行时event的分发。
    # 大白话：嘿，EventCenter，我订阅这些Event，如果有人产生这些Event，请一定给我。
    def _getEventDispatcher(self):
        return {'data_in': self.__ProcessData}

    # 处理data_in事件的handler，私有方法，只对EventCenter“公开”。
    def __ProcessData(self, x):
        print("Processing data [%s]..." % (str(x)))

# *******************************************************************************
# SoftchipApp类是集成者角色.
# 它负责生成soft board和所有的softchip，将二者装配在一起并启动整个系统。
# *******************************************************************************


class SoftchipApp():
    def __init__(self, logger):
        self.logger = logger    # Logger类与主题无关在此略去，不作说明。
        commandMap = {'flush': self.logger.flush, 'tick': self.Tick}
        self.console = ConsolePanel(commandMap)

    def Run(self):
        # *******************************
        # 创建softboard的Binder和Center。
        # *******************************
        self.binder = APIBinder()
        self.center = EventCenter()

        # *******************************
        # 创建各softchip组件。
        # *******************************
        controller = Controller('Disney')
        computer = Computer('Tom')
        processor = Processor('Jerry')

        # *******************************
        # 向API Binder装配必要的softchip。
        # *******************************
        self.binder.PlugChip(controller)  # 向binder插入chip。
        self.binder.PlugChip(computer)  # 向binder插入chip。
        self.binder.Bind()  # 实施API绑定。
        # 绑定完成后检查绑定是否成功。
        if (not (controller.isBindOK() and computer.isBindOK())):
            print("Failed in binding")
            return

        # *********************************
        # 向Event Center装配必要的softchip。
        # *********************************
        controller.SetCenter(self.center)
        processor.SetCenter(self.center)
        self.center.PlugChip(controller)  # 向center插入chip
        self.center.PlugChip(processor)  # 向center插入chip

        # *********************************
        # 装配完毕，启动整个application
        # *********************************
        # console组件是非关键性部分，在此略去。
        # 其主要功能是定时向EventCenter送出tick事件。
        self.console.Start()

    def Tick(self):
        self.center.ProcessEvent('tick')
if __name__ == "__main__":

    A=SoftchipApp
    A.Run()