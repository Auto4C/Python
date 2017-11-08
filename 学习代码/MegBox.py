# 简化所有的提示和消息窗口

from PyQt5.QtWidgets import QMessageBox


def Warning(message):
#警告信息窗口，模态
    QMessageBox.information(None, ("Warning!"), message, QMessageBox.StandardButton(QMessageBox.Ok))