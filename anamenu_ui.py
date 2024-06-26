# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anamenu_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Anamenu(object):
    def setupUi(self, Anamenu):
        Anamenu.setObjectName("Anamenu")
        Anamenu.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Anamenu.sizePolicy().hasHeightForWidth())
        Anamenu.setSizePolicy(sizePolicy)
        Anamenu.setMinimumSize(QtCore.QSize(640, 480))
        Anamenu.setMaximumSize(QtCore.QSize(640, 480))
        Anamenu.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon( )
        icon.addPixmap(QtGui.QPixmap("src/logos/birimcevirici.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Anamenu.setWindowIcon(icon)
        Anamenu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Anamenu)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 150, 561, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_birimcevir = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_birimcevir.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_birimcevir.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_birimcevir.setStyleSheet("background-image: url(src/logos/birimcevirici.png);")
        self.pushButton_birimcevir.setText("")
        self.pushButton_birimcevir.setObjectName("pushButton_birimcevir")
        self.horizontalLayout.addWidget(self.pushButton_birimcevir)
        self.pushButton_bilgi = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_bilgi.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_bilgi.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_bilgi.setStyleSheet("background-image: url(src/logos/bilgi.png);")
        self.pushButton_bilgi.setText("")
        self.pushButton_bilgi.setObjectName("pushButton_bilgi")
        self.horizontalLayout.addWidget(self.pushButton_bilgi)
        self.pushButton_cikis = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_cikis.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_cikis.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_cikis.setStyleSheet("background-image: url(src/logos/exit.png);")
        self.pushButton_cikis.setText("")
        self.pushButton_cikis.setObjectName("pushButton_cikis")
        self.horizontalLayout.addWidget(self.pushButton_cikis)
        self.label_birimcevirici = QtWidgets.QLabel(Anamenu)
        self.label_birimcevirici.setGeometry(QtCore.QRect(60, 60, 501, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_birimcevirici.sizePolicy().hasHeightForWidth())
        self.label_birimcevirici.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Formula1 Display Bold")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_birimcevirici.setFont(font)
        self.label_birimcevirici.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_birimcevirici.setAutoFillBackground(False)
        self.label_birimcevirici.setAlignment(QtCore.Qt.AlignCenter)
        self.label_birimcevirici.setObjectName("label_birimcevirici")
        self.label_birimcevir = QtWidgets.QLabel(Anamenu)
        self.label_birimcevir.setGeometry(QtCore.QRect(90, 260, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Formula1")
        font.setPointSize(12)
        self.label_birimcevir.setFont(font)
        self.label_birimcevir.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_birimcevir.setAlignment(QtCore.Qt.AlignCenter)
        self.label_birimcevir.setObjectName("label_birimcevir")
        self.label_bilgi = QtWidgets.QLabel(Anamenu)
        self.label_bilgi.setGeometry(QtCore.QRect(260, 260, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Formula1")
        font.setPointSize(12)
        self.label_bilgi.setFont(font)
        self.label_bilgi.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_bilgi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bilgi.setObjectName("label_bilgi")
        self.label_cikis = QtWidgets.QLabel(Anamenu)
        self.label_cikis.setGeometry(QtCore.QRect(430, 260, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Formula1")
        font.setPointSize(12)
        self.label_cikis.setFont(font)
        self.label_cikis.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_cikis.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cikis.setObjectName("label_cikis")

        self.retranslateUi(Anamenu)
        QtCore.QMetaObject.connectSlotsByName(Anamenu)

    def retranslateUi(self, Anamenu):
        _translate = QtCore.QCoreApplication.translate
        Anamenu.setWindowTitle(_translate("Anamenu", "Birim Çevirici"))
        self.label_birimcevirici.setText(_translate("Anamenu", "BİRİM ÇEVİRİCİ"))
        self.label_birimcevir.setText(_translate("Anamenu", "BİRİM ÇEVİR"))
        self.label_bilgi.setText(_translate("Anamenu", "BİLGİ"))
        self.label_cikis.setText(_translate("Anamenu", "ÇIKIŞ"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Anamenu = QtWidgets.QDialog()
    ui = Ui_Anamenu()
    ui.setupUi(Anamenu)
    Anamenu.show()
    sys.exit(app.exec_())
