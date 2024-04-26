# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kondansator_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_kondansator(object):
    def setupUi(self, kondansator):
        kondansator.setObjectName("kondansator")
        kondansator.resize(640, 480)
        kondansator.setMinimumSize(QtCore.QSize(640, 480))
        kondansator.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setFamily("Formula1")
        font.setPointSize(10)
        kondansator.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/logos/birimcevirici.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        kondansator.setWindowIcon(icon)
        self.groupBox_kondansator = QtWidgets.QGroupBox(kondansator)
        self.groupBox_kondansator.setGeometry(QtCore.QRect(80, 50, 471, 361))
        font = QtGui.QFont()
        font.setFamily("Formula1")
        font.setPointSize(14)
        self.groupBox_kondansator.setFont(font)
        self.groupBox_kondansator.setObjectName("groupBox_kondansator")
        self.pushButton_hesapla_kondansator = QtWidgets.QPushButton(self.groupBox_kondansator)
        self.pushButton_hesapla_kondansator.setGeometry(QtCore.QRect(290, 210, 151, 51))
        self.pushButton_hesapla_kondansator.setObjectName("pushButton_hesapla_kondansator")
        self.comboBox_giris_kondansator = QtWidgets.QComboBox(self.groupBox_kondansator)
        self.comboBox_giris_kondansator.setGeometry(QtCore.QRect(230, 120, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_giris_kondansator.setFont(font)
        self.comboBox_giris_kondansator.setObjectName("comboBox_giris_kondansator")
        self.comboBox_giris_kondansator.addItem("")
        self.comboBox_giris_kondansator.addItem("")
        self.comboBox_giris_kondansator.addItem("")
        self.comboBox_giris_kondansator.addItem("")
        self.lineEdit_giris_kondansator = QtWidgets.QLineEdit(self.groupBox_kondansator)
        self.lineEdit_giris_kondansator.setGeometry(QtCore.QRect(90, 120, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_giris_kondansator.setFont(font)
        self.lineEdit_giris_kondansator.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_giris_kondansator.setObjectName("lineEdit_giris_kondansator")
        self.label_cikis_kondansator = QtWidgets.QLabel(self.groupBox_kondansator)
        self.label_cikis_kondansator.setGeometry(QtCore.QRect(190, 290, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cikis_kondansator.setFont(font)
        self.label_cikis_kondansator.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cikis_kondansator.setObjectName("label_cikis_kondansator")
        self.label_giris_kondansator = QtWidgets.QLabel(self.groupBox_kondansator)
        self.label_giris_kondansator.setGeometry(QtCore.QRect(170, 90, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_giris_kondansator.setFont(font)
        self.label_giris_kondansator.setAlignment(QtCore.Qt.AlignCenter)
        self.label_giris_kondansator.setObjectName("label_giris_kondansator")
        self.lineEdit_cikis_kondansator = QtWidgets.QLineEdit(self.groupBox_kondansator)
        self.lineEdit_cikis_kondansator.setGeometry(QtCore.QRect(150, 310, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_cikis_kondansator.setFont(font)
        self.lineEdit_cikis_kondansator.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_cikis_kondansator.setObjectName("lineEdit_cikis_kondansator")
        self.comboBox_cikis_kondansator = QtWidgets.QComboBox(self.groupBox_kondansator)
        self.comboBox_cikis_kondansator.setGeometry(QtCore.QRect(130, 210, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_cikis_kondansator.setFont(font)
        self.comboBox_cikis_kondansator.setObjectName("comboBox_cikis_kondansator")
        self.comboBox_cikis_kondansator.addItem("")
        self.comboBox_cikis_kondansator.addItem("")
        self.comboBox_cikis_kondansator.addItem("")
        self.comboBox_cikis_kondansator.addItem("")
        self.label_cikisb_kondansator = QtWidgets.QLabel(self.groupBox_kondansator)
        self.label_cikisb_kondansator.setGeometry(QtCore.QRect(40, 210, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cikisb_kondansator.setFont(font)
        self.label_cikisb_kondansator.setObjectName("label_cikisb_kondansator")
        self.pushButton_menuyedon_kondansator = QtWidgets.QPushButton(kondansator)
        self.pushButton_menuyedon_kondansator.setGeometry(QtCore.QRect(560, 400, 50, 50))
        self.pushButton_menuyedon_kondansator.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_menuyedon_kondansator.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_menuyedon_kondansator.setStyleSheet("background-image: url(src/logos/exit2.png);")
        self.pushButton_menuyedon_kondansator.setText("")
        self.pushButton_menuyedon_kondansator.setObjectName("pushButton_menuyedon_kondansator")
        self.label_menuyedon_kondansator = QtWidgets.QLabel(kondansator)
        self.label_menuyedon_kondansator.setGeometry(QtCore.QRect(550, 450, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Formula1")
        font.setPointSize(6)
        self.label_menuyedon_kondansator.setFont(font)
        self.label_menuyedon_kondansator.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_menuyedon_kondansator.setAlignment(QtCore.Qt.AlignCenter)
        self.label_menuyedon_kondansator.setObjectName("label_menuyedon_kondansator")
        self.pushButton_bilgi = QtWidgets.QPushButton(kondansator)
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

        self.retranslateUi(kondansator)
        QtCore.QMetaObject.connectSlotsByName(kondansator)

    def retranslateUi(self, kondansator):
        _translate = QtCore.QCoreApplication.translate
        kondansator.setWindowTitle(_translate("kondansator", "Birim Çevirici - Kondansatör"))
        self.groupBox_kondansator.setTitle(_translate("kondansator", "Kondansatör Çevirme Menüsü"))
        self.pushButton_hesapla_kondansator.setText(_translate("kondansator", "HESAPLA"))
        self.comboBox_giris_kondansator.setItemText(0, _translate("kondansator", "farad"))
        self.comboBox_giris_kondansator.setItemText(1, _translate("kondansator", "microfarad"))
        self.comboBox_giris_kondansator.setItemText(2, _translate("kondansator", "nanofarad"))
        self.comboBox_giris_kondansator.setItemText(3, _translate("kondansator", "picofarad"))
        self.label_cikis_kondansator.setText(_translate("kondansator", "Çıkış Değeri"))
        self.label_giris_kondansator.setText(_translate("kondansator", "Giriş Değeri"))
        self.comboBox_cikis_kondansator.setItemText(0, _translate("kondansator", "farad"))
        self.comboBox_cikis_kondansator.setItemText(1, _translate("kondansator", "microfarad"))
        self.comboBox_cikis_kondansator.setItemText(2, _translate("kondansator", "nanofarad"))
        self.comboBox_cikis_kondansator.setItemText(3, _translate("kondansator", "picofarad"))
        self.label_cikisb_kondansator.setText(_translate("kondansator", "Çıkış Birimi:"))
        self.label_menuyedon_kondansator.setText(_translate("kondansator", "MENÜYE DÖN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kondansator = QtWidgets.QDialog()
    ui = Ui_kondansator()
    ui.setupUi(kondansator)
    kondansator.show()
    sys.exit(app.exec_())
