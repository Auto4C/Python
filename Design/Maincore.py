# 导入自定义
from 学习代码 import MegBox
from Design import UIcore
# 导入系统
from PyQt5 import QtWidgets
import sys

# 这段主程序创建了一个新的QtWidgets应用，每个Qt应用都可以通过命令行进行配置（需传入sys.argv参数）

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UIcore.LoadWin()
    window.show()
    # MegBox.Warning("警告：提示信息窗口，该窗口为模态！")  # 快速使用CHJ简化的MegBox 属于Maincore的子函数
    sys.exit(app.exec_())  # 系统退出关闭app
# 定义响应函数


def Calc(price,tax):

    if price is None:
        price = 1
    total_price = tax * price
    total_price_string = "乘法结果是: " + str(total_price)
    return total_price_string
