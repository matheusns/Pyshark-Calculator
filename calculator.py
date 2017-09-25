# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shark_calculator.ui'
#
# Created: Fri Feb 10 14:58:53 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        MainWindow.setMaximumSize(QtCore.QSize(900, 700))
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/shark-305004_640.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.calcular_bt = QtGui.QPushButton(self.centralwidget)
        self.calcular_bt.setGeometry(QtCore.QRect(40, 620, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.calcular_bt.setFont(font)
        self.calcular_bt.setObjectName(_fromUtf8("calcular_bt"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 871, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 60, 831, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.limpar_bt = QtGui.QPushButton(self.centralwidget)
        self.limpar_bt.setGeometry(QtCore.QRect(170, 620, 111, 31))
        self.limpar_bt.setObjectName(_fromUtf8("limpar_bt"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.variaveis = QtGui.QLineEdit(self.centralwidget)
        self.variaveis.setGeometry(QtCore.QRect(40, 180, 321, 27))
        self.variaveis.setObjectName(_fromUtf8("variaveis"))
        self.atribuir_bt = QtGui.QPushButton(self.centralwidget)
        self.atribuir_bt.setGeometry(QtCore.QRect(40, 210, 111, 31))
        self.atribuir_bt.setObjectName(_fromUtf8("atribuir_bt"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 560, 141, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lista = QtGui.QListWidget(self.centralwidget)
        self.lista.setGeometry(QtCore.QRect(40, 250, 321, 301))
        self.lista.setObjectName(_fromUtf8("lista"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 839, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.expr = QtGui.QLineEdit(self.centralwidget)
        self.expr.setGeometry(QtCore.QRect(40, 120, 831, 27))
        self.expr.setObjectName(_fromUtf8("expr"))
        self.result_list = QtGui.QListWidget(self.centralwidget)
        self.result_list.setGeometry(QtCore.QRect(391, 180, 481, 131))
        self.result_list.setObjectName(_fromUtf8("result_list"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 155, 469, 23))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 10, 101, 51))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("icons/shark-305004_640.png")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(390, 330, 481, 341))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tlwg Typo"))
        font.setUnderline(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet(_fromUtf8("border-color: rgb(0, 0, 0);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(23)
        self.frame.setMidLineWidth(11)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 221, 271))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8(""))
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(250, 60, 221, 271))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8(""))
        self.label_7.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(130, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 300, 121, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.limpar_bt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.variaveis.clear)
        QtCore.QObject.connect(self.calcular_bt, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.calcular)
        QtCore.QObject.connect(self.atribuir_bt, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.atrib)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lista.clear)
        QtCore.QObject.connect(self.limpar_bt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.expr.clear)
        QtCore.QObject.connect(self.limpar_bt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.result_list.clear)
        QtCore.QObject.connect(self.atribuir_bt, QtCore.SIGNAL(_fromUtf8("clicked()")), self.variaveis.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Power Pyshark Calculator", None))
        self.calcular_bt.setText(_translate("MainWindow", "EVALUATE", None))
        self.label_2.setText(_translate("MainWindow", "Power Pyshark- Scientific Expressions Calculator", None))
        self.limpar_bt.setText(_translate("MainWindow", "Clean All", None))
        self.label_4.setText(_translate("MainWindow", "Assignment of variables:", None))
        self.atribuir_bt.setText(_translate("MainWindow", "Assign", None))
        self.pushButton.setText(_translate("MainWindow", "Clean history", None))
        self.label.setText(_translate("MainWindow", "Type your expression:", None))
        self.label_5.setText(_translate("MainWindow", "Results:", None))
        self.label_3.setText(_translate("MainWindow", "Multiplication: \' * \' \n"
"\n"
"Division: \' / \' \n"
"\n"
"Sum: \' + \' \n"
"\n"
"Subtraction: \' - \'\n"
"\n"
"Exponentiation: \' ** \'\n"
"\n"
"Square Root: sqrt()\n"
"\n"
"Factorial: \' ! \'", None))
        self.label_7.setText(_translate("MainWindow", "Limit: \' limit() \' \n"
"\n"
"Derivative: \' diff() \' \n"
"\n"
"Integral: \' integrate ()\'", None))
        self.label_8.setText(_translate("MainWindow", "OPERATORS", None))
        self.pushButton_2.setText(_translate("MainWindow", "EXAMPLES", None))

