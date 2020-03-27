# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/lubel/Documents/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_TypingGame(object):
    def setupUi(self, TypingGame):
        TypingGame.setObjectName("TypingGame")
        TypingGame.resize(800, 600)
        TypingGame.setFixedSize(800,600)
        self.centralwidget = QtWidgets.QWidget(TypingGame)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 571))
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn_generate = QtWidgets.QPushButton(self.tab)
        self.btn_generate.setGeometry(QtCore.QRect(40, 350, 161, 28))
        self.btn_generate.setObjectName("btn_generate")
        self.btn_generate.clicked.connect(self.generate)
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(13, 400, 771, 120))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(self.checker)
        self.label_error = QtWidgets.QLabel(self.tab)
        self.label_error.setGeometry(QtCore.QRect(620, 350, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_error.setFont(font)
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 761, 320))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFontPointSize(12)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ptedit_charset = QtWidgets.QPlainTextEdit(self.tab_2)
        self.ptedit_charset.setGeometry(QtCore.QRect(20, 30, 751, 75))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ptedit_charset.setFont(font)
        self.ptedit_charset.setObjectName("ptedit_charset")
        self.ptedit_charset.setPlainText("qwertyuiopas dfghjklzxcvbm")
        self.ptedit_charset.textChanged.connect(self.changer)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 130, 90, 28))
        self.pushButton.setStatusTip("")
        self.pushButton.setWhatsThis("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.default)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(30, 10, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 141, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 210, 113, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('700')
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 210, 90, 28))
        self.pushButton_2.setStatusTip("")
        self.pushButton_2.setWhatsThis("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.maxchar)
        self.tabWidget.addTab(self.tab_2, "")
        TypingGame.setCentralWidget(self.centralwidget)
        #self.menubar = QtWidgets.QMenuBar(TypingGame)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        #self.menubar.setObjectName("menubar")
        #self.menuHelpy = QtWidgets.QMenu(self.menubar)
        #self.menuHelpy.setObjectName("menuHelpy")
        #TypingGame.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TypingGame)
        self.statusbar.setObjectName("statusbar")
        TypingGame.setStatusBar(self.statusbar)
        #self.menubar.addAction(self.menuHelpy.menuAction())

        self.retranslateUi(TypingGame)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TypingGame)

    def retranslateUi(self, TypingGame):
        _translate = QtCore.QCoreApplication.translate
        TypingGame.setWindowTitle(_translate("TypingGame", "Typing Practice"))
        self.btn_generate.setText(_translate("TypingGame", "Generate Random Text"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("TypingGame", "Game"))
        #self.ptedit_charset.setPlainText(_translate("TypingGame", "q,w,e,r,t,y,u,i,o,p,a,s, ,d,f,g,h,j,k,l,z,x,c,v,b,n,m"))
        self.pushButton.setText(_translate("TypingGame", "Default"))
        self.label.setText(_translate("TypingGame", "List of characters:"))
        self.label_2.setText(_translate("TypingGame", "Max characters:"))
        self.pushButton_2.setText(_translate("TypingGame", "Set Max Char"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("TypingGame", "Settings"))
        #self.menuHelpy.setTitle(_translate("TypingGame", "Help"))
    def default(self):
        self.ptedit_charset.setPlainText("qwertyuiopas dfghjklzxcvbm")
    def changer(self):
        character_set = self.ptedit_charset.toPlainText()
        return list(character_set)
    def maxchar(self):
         while True:
            try:
                maxcharacter = int(self.lineEdit.text())
            except:
                self.lineEdit.setText('700')
                continue
            else:
                maxcharacter = int(self.lineEdit.text())
                return maxcharacter
                break
    def generate(self):
        maxcharacter = self.maxchar()
        self.generated_text = []
        character_set = self.changer()
        for i in range(maxcharacter):
            i = random.choice(character_set)
            self.generated_text.append(i)
        self.textBrowser.setText(''.join(self.generated_text))
    def checker(self):
        inputlist = list(self.textEdit.toPlainText())
        print(inputlist)
        for n in range(len(inputlist)):
            if inputlist[n] == self.generated_text[n]:
                self.label_error.setText("")
            else:
                self.label_error.setText("ERROR")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TypingGame = QtWidgets.QMainWindow()
    ui = Ui_TypingGame()
    ui.setupUi(TypingGame)
    TypingGame.show()
    sys.exit(app.exec_())
