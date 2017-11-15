import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

import MegBox


# 使用uic.loadUiType载入界面文件
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
        self.pushButton.clicked.connect(self.CalculateTax)

    # 定义响应函数
    def CalculateTax(self):
        price = int(self.inputbox.toPlainText())
        if price == None:
            price = 1
        tax = (self.spinRate.value())
        total_price = price + ((tax / 100) * price)
        total_price_string = "The total price with tax is: " + str(total_price)
        self.ResultBox.setText(total_price_string)



