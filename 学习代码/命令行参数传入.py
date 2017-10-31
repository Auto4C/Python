#命令行参数输入显示
import sys
import time
#增加窗口
from PyQt5 import QtCore, QtWidgets
#窗口载入
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(400, 100)
widget.setWindowTitle("这是个普通的窗口测试")
widget.show()


