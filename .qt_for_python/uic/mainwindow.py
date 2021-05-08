# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/anupam/Desktop/GITHUB/Minor-2nd-sem/desktop-app/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(508, 259)
        Dialog.setMinimumSize(QtCore.QSize(508, 259))
        Dialog.setMaximumSize(QtCore.QSize(508, 259))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 491, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filelabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.filelabel.setFont(font)
        self.filelabel.setObjectName("filelabel")
        self.horizontalLayout.addWidget(self.filelabel, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.runButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed Light")
        font.setPointSize(13)
        self.runButton.setFont(font)
        self.runButton.setObjectName("runButton")
        self.verticalLayout.addWidget(self.runButton)
        self.logolabel = QtWidgets.QLabel(Dialog)
        self.logolabel.setGeometry(QtCore.QRect(10, 10, 491, 141))
        self.logolabel.setStyleSheet("background-image: url(:/logo/logo.png);")
        self.logolabel.setText("")
        self.logolabel.setPixmap(QtGui.QPixmap("C:/Users/vivek/Downloads/logo.png"))
        self.logolabel.setScaledContents(True)
        self.logolabel.setObjectName("logolabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Face Recognition Time Attendance App"))
        self.filelabel.setText(_translate("Dialog", "Face Recognition Time Attendance App"))
        self.runButton.setText(_translate("Dialog", "Start"))

import resource_rc
