# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setMinimumSize(QtCore.QSize(800, 700))
        MainWindow.setMaximumSize(QtCore.QSize(800, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 700))
        self.tabWidget.setMinimumSize(QtCore.QSize(800, 700))
        self.tabWidget.setMaximumSize(QtCore.QSize(800, 700))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(160, 20, 441, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_30 = QtWidgets.QPushButton(self.tab)
        self.pushButton_30.setGeometry(QtCore.QRect(10, 30, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setObjectName("pushButton_30")
        self.label_82 = QtWidgets.QLabel(self.tab)
        self.label_82.setGeometry(QtCore.QRect(10, 60, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 240, 791, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.colorButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_3.sizePolicy().hasHeightForWidth())
        self.colorButton_3.setSizePolicy(sizePolicy)
        self.colorButton_3.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_3.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_3.setStyleSheet("")
        self.colorButton_3.setText("")
        self.colorButton_3.setObjectName("colorButton_3")
        self.horizontalLayout.addWidget(self.colorButton_3)
        self.label_85 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.horizontalLayout.addWidget(self.label_85)
        self.colorButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_2.sizePolicy().hasHeightForWidth())
        self.colorButton_2.setSizePolicy(sizePolicy)
        self.colorButton_2.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_2.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_2.setStyleSheet("")
        self.colorButton_2.setText("")
        self.colorButton_2.setObjectName("colorButton_2")
        self.horizontalLayout.addWidget(self.colorButton_2)
        self.label_84 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.horizontalLayout.addWidget(self.label_84)
        self.colorButton_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_1.sizePolicy().hasHeightForWidth())
        self.colorButton_1.setSizePolicy(sizePolicy)
        self.colorButton_1.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_1.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_1.setStyleSheet("")
        self.colorButton_1.setText("")
        self.colorButton_1.setObjectName("colorButton_1")
        self.horizontalLayout.addWidget(self.colorButton_1)
        self.label_83 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.horizontalLayout.addWidget(self.label_83)
        self.colorButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_4.sizePolicy().hasHeightForWidth())
        self.colorButton_4.setSizePolicy(sizePolicy)
        self.colorButton_4.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_4.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_4.setStyleSheet("")
        self.colorButton_4.setText("")
        self.colorButton_4.setObjectName("colorButton_4")
        self.horizontalLayout.addWidget(self.colorButton_4)
        self.label_86 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.horizontalLayout.addWidget(self.label_86)
        self.colorButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_5.sizePolicy().hasHeightForWidth())
        self.colorButton_5.setSizePolicy(sizePolicy)
        self.colorButton_5.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_5.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_5.setStyleSheet("")
        self.colorButton_5.setText("")
        self.colorButton_5.setObjectName("colorButton_5")
        self.horizontalLayout.addWidget(self.colorButton_5)
        self.label_87 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_87.setFont(font)
        self.label_87.setObjectName("label_87")
        self.horizontalLayout.addWidget(self.label_87)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(230, 430, 361, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.colorButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_6.sizePolicy().hasHeightForWidth())
        self.colorButton_6.setSizePolicy(sizePolicy)
        self.colorButton_6.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_6.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_6.setStyleSheet("")
        self.colorButton_6.setText("")
        self.colorButton_6.setObjectName("colorButton_6")
        self.horizontalLayout_2.addWidget(self.colorButton_6)
        self.label_88 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_88.setFont(font)
        self.label_88.setObjectName("label_88")
        self.horizontalLayout_2.addWidget(self.label_88)
        self.colorButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_7.sizePolicy().hasHeightForWidth())
        self.colorButton_7.setSizePolicy(sizePolicy)
        self.colorButton_7.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_7.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_7.setStyleSheet("")
        self.colorButton_7.setText("")
        self.colorButton_7.setObjectName("colorButton_7")
        self.horizontalLayout_2.addWidget(self.colorButton_7)
        self.label_89 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_89.setFont(font)
        self.label_89.setObjectName("label_89")
        self.horizontalLayout_2.addWidget(self.label_89)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 570, 761, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(160, 210, 441, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(160, 400, 441, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 60, 331, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.canvas_3 = QtWidgets.QLabel(self.tab)
        self.canvas_3.setGeometry(QtCore.QRect(130, 480, 512, 64))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_3.sizePolicy().hasHeightForWidth())
        self.canvas_3.setSizePolicy(sizePolicy)
        self.canvas_3.setFrameShape(QtWidgets.QFrame.Box)
        self.canvas_3.setLineWidth(2)
        self.canvas_3.setText("")
        self.canvas_3.setObjectName("canvas_3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(130, 480, 511, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.canvas_7 = QtWidgets.QLabel(self.tab)
        self.canvas_7.setGeometry(QtCore.QRect(130, 290, 513, 67))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_7.sizePolicy().hasHeightForWidth())
        self.canvas_7.setSizePolicy(sizePolicy)
        self.canvas_7.setFrameShape(QtWidgets.QFrame.Box)
        self.canvas_7.setLineWidth(2)
        self.canvas_7.setText("")
        self.canvas_7.setObjectName("canvas_7")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(130, 290, 511, 61))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.canvas_8 = QtWidgets.QLabel(self.tab)
        self.canvas_8.setGeometry(QtCore.QRect(130, 100, 512, 64))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_8.sizePolicy().hasHeightForWidth())
        self.canvas_8.setSizePolicy(sizePolicy)
        self.canvas_8.setFrameShape(QtWidgets.QFrame.Box)
        self.canvas_8.setLineWidth(2)
        self.canvas_8.setText("")
        self.canvas_8.setObjectName("canvas_8")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(130, 100, 511, 61))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 441, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_31 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_31.setGeometry(QtCore.QRect(10, 30, 141, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setObjectName("pushButton_31")
        self.label_90 = QtWidgets.QLabel(self.tab_2)
        self.label_90.setGeometry(QtCore.QRect(10, 60, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_90.setFont(font)
        self.label_90.setObjectName("label_90")
        self.canvas_4 = QtWidgets.QLabel(self.tab_2)
        self.canvas_4.setGeometry(QtCore.QRect(120, 290, 512, 64))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_4.sizePolicy().hasHeightForWidth())
        self.canvas_4.setSizePolicy(sizePolicy)
        self.canvas_4.setFrameShape(QtWidgets.QFrame.Box)
        self.canvas_4.setLineWidth(2)
        self.canvas_4.setText("")
        self.canvas_4.setObjectName("canvas_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(160, 210, 441, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 570, 761, 71))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_8.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_7.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_7.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_7.addWidget(self.pushButton_10)
        self.canvas_5 = QtWidgets.QLabel(self.tab_2)
        self.canvas_5.setGeometry(QtCore.QRect(120, 480, 512, 64))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_5.sizePolicy().hasHeightForWidth())
        self.canvas_5.setSizePolicy(sizePolicy)
        self.canvas_5.setFrameShape(QtWidgets.QFrame.Box)
        self.canvas_5.setLineWidth(2)
        self.canvas_5.setText("")
        self.canvas_5.setObjectName("canvas_5")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(440, 60, 331, 27))
        self.pushButton_11.setObjectName("pushButton_11")
        self.canvas_6 = QtWidgets.QLabel(self.tab_2)
        self.canvas_6.setGeometry(QtCore.QRect(120, 110, 512, 64))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas_6.sizePolicy().hasHeightForWidth())
        self.canvas_6.setSizePolicy(sizePolicy)
        self.canvas_6.setFrameShape(QtWidgets.QFrame.Box)
        self.canvas_6.setLineWidth(2)
        self.canvas_6.setText("")
        self.canvas_6.setObjectName("canvas_6")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 240, 791, 51))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.colorButton_15 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_15.sizePolicy().hasHeightForWidth())
        self.colorButton_15.setSizePolicy(sizePolicy)
        self.colorButton_15.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_15.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_15.setStyleSheet("")
        self.colorButton_15.setText("")
        self.colorButton_15.setObjectName("colorButton_15")
        self.horizontalLayout_8.addWidget(self.colorButton_15)
        self.label_98 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_98.setFont(font)
        self.label_98.setObjectName("label_98")
        self.horizontalLayout_8.addWidget(self.label_98)
        self.colorButton_16 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_16.sizePolicy().hasHeightForWidth())
        self.colorButton_16.setSizePolicy(sizePolicy)
        self.colorButton_16.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_16.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_16.setStyleSheet("")
        self.colorButton_16.setText("")
        self.colorButton_16.setObjectName("colorButton_16")
        self.horizontalLayout_8.addWidget(self.colorButton_16)
        self.label_99 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_99.setFont(font)
        self.label_99.setObjectName("label_99")
        self.horizontalLayout_8.addWidget(self.label_99)
        self.colorButton_17 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_17.sizePolicy().hasHeightForWidth())
        self.colorButton_17.setSizePolicy(sizePolicy)
        self.colorButton_17.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_17.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_17.setStyleSheet("")
        self.colorButton_17.setText("")
        self.colorButton_17.setObjectName("colorButton_17")
        self.horizontalLayout_8.addWidget(self.colorButton_17)
        self.label_100 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_100.setFont(font)
        self.label_100.setObjectName("label_100")
        self.horizontalLayout_8.addWidget(self.label_100)
        self.colorButton_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_18.sizePolicy().hasHeightForWidth())
        self.colorButton_18.setSizePolicy(sizePolicy)
        self.colorButton_18.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_18.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_18.setStyleSheet("")
        self.colorButton_18.setText("")
        self.colorButton_18.setObjectName("colorButton_18")
        self.horizontalLayout_8.addWidget(self.colorButton_18)
        self.label_101 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_101.setFont(font)
        self.label_101.setObjectName("label_101")
        self.horizontalLayout_8.addWidget(self.label_101)
        self.colorButton_19 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_19.sizePolicy().hasHeightForWidth())
        self.colorButton_19.setSizePolicy(sizePolicy)
        self.colorButton_19.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_19.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_19.setStyleSheet("")
        self.colorButton_19.setText("")
        self.colorButton_19.setObjectName("colorButton_19")
        self.horizontalLayout_8.addWidget(self.colorButton_19)
        self.label_102 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_102.setFont(font)
        self.label_102.setObjectName("label_102")
        self.horizontalLayout_8.addWidget(self.label_102)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(230, 430, 361, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.colorButton_20 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_20.sizePolicy().hasHeightForWidth())
        self.colorButton_20.setSizePolicy(sizePolicy)
        self.colorButton_20.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_20.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_20.setStyleSheet("")
        self.colorButton_20.setText("")
        self.colorButton_20.setObjectName("colorButton_20")
        self.horizontalLayout_9.addWidget(self.colorButton_20)
        self.label_103 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_103.setFont(font)
        self.label_103.setObjectName("label_103")
        self.horizontalLayout_9.addWidget(self.label_103)
        self.colorButton_21 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_21.sizePolicy().hasHeightForWidth())
        self.colorButton_21.setSizePolicy(sizePolicy)
        self.colorButton_21.setMinimumSize(QtCore.QSize(20, 20))
        self.colorButton_21.setMaximumSize(QtCore.QSize(40, 40))
        self.colorButton_21.setStyleSheet("")
        self.colorButton_21.setText("")
        self.colorButton_21.setObjectName("colorButton_21")
        self.horizontalLayout_9.addWidget(self.colorButton_21)
        self.label_104 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_104.setFont(font)
        self.label_104.setObjectName("label_104")
        self.horizontalLayout_9.addWidget(self.label_104)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(160, 400, 441, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Разметка новых магнитограмм"))
        self.pushButton_30.setText(_translate("MainWindow", "Выбрать файл"))
        self.label_82.setText(_translate("MainWindow", "Файл не выбран"))
        self.label_85.setText(_translate("MainWindow", "Зеленый"))
        self.label_84.setText(_translate("MainWindow", "Синий"))
        self.label_83.setText(_translate("MainWindow", "Желтый"))
        self.label_86.setText(_translate("MainWindow", "Черный"))
        self.label_87.setText(_translate("MainWindow", "Голубой"))
        self.label_88.setText(_translate("MainWindow", "Зеленый"))
        self.label_89.setText(_translate("MainWindow", "Красный"))
        self.pushButton.setText(_translate("MainWindow", "Очистить поле для объектов"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить поле для дефектов"))
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить изображения"))
        self.label_3.setText(_translate("MainWindow", "Разметка объектов"))
        self.label_4.setText(_translate("MainWindow", "Разметка дефектов"))
        self.pushButton_4.setText(_translate("MainWindow", "Получить ответ от нейронной сети"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  _translate("MainWindow", "Разметка новых магнитограмм"))
        self.label_2.setText(_translate("MainWindow", "Практика"))
        self.pushButton_31.setText(_translate("MainWindow", "Выбрать задание"))
        self.label_90.setText(_translate("MainWindow", "Файл не выбран"))
        self.label_5.setText(_translate("MainWindow", "Разметка объектов"))
        self.pushButton_8.setText(_translate("MainWindow", "Очистить поле для объектов"))
        self.pushButton_9.setText(_translate("MainWindow", "Очистить поле для дефектов"))
        self.pushButton_10.setText(_translate("MainWindow", "Проверить результат"))
        self.pushButton_11.setText(_translate("MainWindow", "Получить ответ от нейронной сети"))
        self.label_98.setText(_translate("MainWindow", "Зеленый"))
        self.label_99.setText(_translate("MainWindow", "Синий"))
        self.label_100.setText(_translate("MainWindow", "Желтый"))
        self.label_101.setText(_translate("MainWindow", "Черный"))
        self.label_102.setText(_translate("MainWindow", "Голубой"))
        self.label_103.setText(_translate("MainWindow", "Зеленый"))
        self.label_104.setText(_translate("MainWindow", "Красный"))
        self.label_6.setText(_translate("MainWindow", "Разметка дефектов"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Практика"))

        self.colorButton_3.setStyleSheet('background-color: rgb(0, 128, 0); ')
        self.colorButton_2.setStyleSheet('background-color: rgb(0, 0, 255); ')
        self.colorButton_1.setStyleSheet('background-color: rgb(255, 255, 0); ')
        self.colorButton_4.setStyleSheet('background-color: rgb(0, 0, 0); ')
        self.colorButton_5.setStyleSheet('background-color: rgb(0, 255, 255); ')
        self.colorButton_6.setStyleSheet('background-color: rgb(0, 128, 0); ')
        self.colorButton_7.setStyleSheet('background-color: rgb(255, 0, 0); ')
        self.canvas_3.setStyleSheet('background-color: rgb(0, 128, 0); ')
        self.canvas_7.setStyleSheet('background-color: rgb(0, 128, 0); ')
        self.gridLayout_5.setGeometry(QRect(130, 100, 512, 64))
        self.gridLayout_4.setGeometry(QRect(130, 290, 513, 67))
        self.gridLayout_2.setGeometry(QRect(130, 480, 512, 64))
