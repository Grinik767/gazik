import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyui.design_1 import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.colorButton_3.setStyleSheet('background-color: rgb(0, 128, 0); ')
        self.colorButton_2.setStyleSheet('background-color: rgb(0, 0, 255); ')
        self.colorButton_1.setStyleSheet('background-color: rgb(255, 255, 0); ')
        self.colorButton_4.setStyleSheet('background-color: rgb(0, 0, 0); ')
        self.colorButton_5.setStyleSheet('background-color: rgb(0, 255, 255); ')
        self.colorButton_6.setStyleSheet('background-color: rgb(0, 128, 0); ')
        self.colorButton_7.setStyleSheet('background-color: rgb(255, 0, 0); ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
