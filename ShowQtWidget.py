import sys
from PyQt5 import QtCore, QtWidgets

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(400, 100)
widget.setWindowTitle("这是个普通的窗口测试")
widget.show()

exit(app.exec_())