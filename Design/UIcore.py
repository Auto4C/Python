
from PyQt5 import QtCore, QtGui, QtWidgets, uic
# import Maincore # Python是可以相互import的（但不建议使用该方式）

# 使用uic.loadUiType载入界面文件
from Design.UIEvent import UIeve

ui_filename = 'testui_1.ui'  # 文件名称，相对于项目路径

Ui_MainWindow, QtBaseClass = uic.loadUiType(ui_filename)
# 创建类LoadWin类继承于Qt库并且调用了父类的初始化函数


class LoadWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #
        self.pushButton.setToolTip("QQQ")  # 修改提示文本
        # 定义界面按钮的单击动作链接的执行函数
        self.pushButton.clicked.connect(self.Bevent)

    # 定义响应函数
    def Bevent(self):
        price = int(self.inputbox.toPlainText())
        # if price == None:
        #     price = 1
        tax = (self.spinRate.value())
        # total_price = price + ((tax / 100) * price)
        # total_price_string = Maincore.Calc(price, tax)
        calc=UIeve("add")
        total_price_string=calc._Result("sss")
        self.ResultBox.setText(total_price_string)
