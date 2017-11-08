# QT的界面显示

import time
import sys
from PyQt5 import QtCore, QtWidgets

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(400, 100)
widget.setWindowTitle("这是个普通的窗口测试")
widget.show()

widget.setWindowTitle("普通的窗口测试")
exit(app.exec_())
