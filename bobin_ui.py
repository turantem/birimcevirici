# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bobin_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bobin(object):
    def setupUi(self, bobin):
        bobin.setObjectName("bobin")
        bobin.resize(640, 480)
        bobin.setMinimumSize(QtCore.QSize(640, 480))
        bobin.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/logos/birimcevirici.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        bobin.setWindowIcon(icon)
        self.groupBox_bobin = QtWidgets.QGroupBox(bobin)
        self.groupBox_bobin.setGeometry(QtCore.QRect(80, 50, 471, 361))
        font = QtGui.QFont()
        font.setFamily("Formula1")
        font.setPointSize(14)
        self.groupBox_bobin.setFont(font)
        self.groupBox_bobin.setObjectName("groupBox_bobin")
        self.pushButton_hesapla_bobin = QtWidgets.QPushButton(self.groupBox_bobin)
        self.pushButton_hesapla_bobin.setGeometry(QtCore.QRect(290, 210, 151, 51))
        self.pushButton_hesapla_bobin.setObjectName("pushButton_hesapla_bobin")
        self.comboBox_giris_bobin = QtWidgets.QComboBox(self.groupBox_bobin)
        self.comboBox_giris_bobin.setGeometry(QtCore.QRect(230, 120, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_giris_bobin.setFont(font)
        self.comboBox_giris_bobin.setObjectName("comboBox_giris_bobin")
        self.comboBox_giris_bobin.addItem("")
        self.comboBox_giris_bobin.addItem("")
        self.comboBox_giris_bobin.addItem("")
        self.comboBox_giris_bobin.addItem("")
        self.comboBox_giris_bobin.addItem("")
        self.comboBox_giris_bobin.addItem("")
        self.comboBox_giris_bobin.addItem("")
        self.lineEdit_giris_bobin = QtWidgets.QLineEdit(self.groupBox_bobin)
        self.lineEdit_giris_bobin.setGeometry(QtCore.QRect(90, 120, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_giris_bobin.setFont(font)
        self.lineEdit_giris_bobin.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_giris_bobin.setObjectName("lineEdit_giris_bobin")
        self.label_cikis_bobin = QtWidgets.QLabel(self.groupBox_bobin)
        self.label_cikis_bobin.setGeometry(QtCore.QRect(190, 290, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cikis_bobin.setFont(font)
        self.label_cikis_bobin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cikis_bobin.setObjectName("label_cikis_bobin")
        self.label_giris_bobin = QtWidgets.QLabel(self.groupBox_bobin)
        self.label_giris_bobin.setGeometry(QtCore.QRect(170, 90, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_giris_bobin.setFont(font)
        self.label_giris_bobin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_giris_bobin.setObjectName("label_giris_bobin")
        self.lineEdit_cikis_bobin = QtWidgets.QLineEdit(self.groupBox_bobin)
        self.lineEdit_cikis_bobin.setGeometry(QtCore.QRect(150, 310, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_cikis_bobin.setFont(font)
        self.lineEdit_cikis_bobin.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_cikis_bobin.setObjectName("lineEdit_cikis_bobin")
        self.comboBox_giris_bobin_2 = QtWidgets.QComboBox(self.groupBox_bobin)
        self.comboBox_giris_bobin_2.setGeometry(QtCore.QRect(130, 210, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_giris_bobin_2.setFont(font)
        self.comboBox_giris_bobin_2.setObjectName("comboBox_giris_bobin_2")
        self.comboBox_giris_bobin_2.addItem("")
        self.comboBox_giris_bobin_2.addItem("")
        self.comboBox_giris_bobin_2.addItem("")
        self.comboBox_giris_bobin_2.addItem("")
        self.comboBox_giris_bobin_2.addItem("")
        self.comboBox_giris_bobin_2.addItem("")
        self.comboBox_giris_bobin_2.addItem("")
        self.label_cikis_bobin_2 = QtWidgets.QLabel(self.groupBox_bobin)
        self.label_cikis_bobin_2.setGeometry(QtCore.QRect(40, 210, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cikis_bobin_2.setFont(font)
        self.label_cikis_bobin_2.setObjectName("label_cikis_bobin_2")
        self.pushButton_menuyedon_bobin = QtWidgets.QPushButton(bobin)
        self.pushButton_menuyedon_bobin.setGeometry(QtCore.QRect(560, 400, 50, 50))
        self.pushButton_menuyedon_bobin.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_menuyedon_bobin.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_menuyedon_bobin.setStyleSheet("background-image: url(src/logos/exit2.png);")
        self.pushButton_menuyedon_bobin.setText("")
        self.pushButton_menuyedon_bobin.setObjectName("pushButton_menuyedon_bobin")
        self.label_menuyedon_bobin = QtWidgets.QLabel(bobin)
        self.label_menuyedon_bobin.setGeometry(QtCore.QRect(550, 450, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Formula1")
        font.setPointSize(6)
        self.label_menuyedon_bobin.setFont(font)
        self.label_menuyedon_bobin.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_menuyedon_bobin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_menuyedon_bobin.setObjectName("label_menuyedon_bobin")
        self.pushButton_bilgi = QtWidgets.QPushButton(bobin)
        self.pushButton_bilgi.setGeometry(QtCore.QRect(10, 450, 20, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_bilgi.sizePolicy().hasHeightForWidth())
        self.pushButton_bilgi.setSizePolicy(sizePolicy)
        self.pushButton_bilgi.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_bilgi.setStyleSheet("QPushButton {\n"
"\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background-image: url(src/logos/info2.png);\n"
"    padding: 5px;\n"
"    }\n"
"    ")
        self.pushButton_bilgi.setText("")
        self.pushButton_bilgi.setObjectName("pushButton_bilgi")

        self.retranslateUi(bobin)
        QtCore.QMetaObject.connectSlotsByName(bobin)

    def retranslateUi(self, bobin):
        _translate = QtCore.QCoreApplication.translate
        bobin.setWindowTitle(_translate("bobin", "Birim Çevirici - Bobin"))
        self.groupBox_bobin.setTitle(_translate("bobin", "Bobin Çevirme Menüsü"))
        self.pushButton_hesapla_bobin.setText(_translate("bobin", "HESAPLA"))
        self.comboBox_giris_bobin.setItemText(0, _translate("bobin", "gigahenry"))
        self.comboBox_giris_bobin.setItemText(1, _translate("bobin", "megahenry"))
        self.comboBox_giris_bobin.setItemText(2, _translate("bobin", "kilohenry"))
        self.comboBox_giris_bobin.setItemText(3, _translate("bobin", "henry"))
        self.comboBox_giris_bobin.setItemText(4, _translate("bobin", "milihenry"))
        self.comboBox_giris_bobin.setItemText(5, _translate("bobin", "mikrohenry"))
        self.comboBox_giris_bobin.setItemText(6, _translate("bobin", "nanohenry"))
        self.label_cikis_bobin.setText(_translate("bobin", "Çıkış Değeri"))
        self.label_giris_bobin.setText(_translate("bobin", "Giriş Değeri"))
        self.comboBox_giris_bobin_2.setItemText(0, _translate("bobin", "gigahenry"))
        self.comboBox_giris_bobin_2.setItemText(1, _translate("bobin", "megahenry"))
        self.comboBox_giris_bobin_2.setItemText(2, _translate("bobin", "kilohenry"))
        self.comboBox_giris_bobin_2.setItemText(3, _translate("bobin", "henry"))
        self.comboBox_giris_bobin_2.setItemText(4, _translate("bobin", "milihenry"))
        self.comboBox_giris_bobin_2.setItemText(5, _translate("bobin", "mikrohenry"))
        self.comboBox_giris_bobin_2.setItemText(6, _translate("bobin", "nanohenry"))
        self.label_cikis_bobin_2.setText(_translate("bobin", "Çıkış Birimi:"))
        self.label_menuyedon_bobin.setText(_translate("bobin", "MENÜYE DÖN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bobin = QtWidgets.QDialog()
    ui = Ui_bobin()
    ui.setupUi(bobin)
    bobin.show()
    sys.exit(app.exec_())
