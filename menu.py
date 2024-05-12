from PyQt5.QtWidgets import *
from anamenu_ui import Ui_Anamenu
from bilgi_ui import Ui_bilgi
from birimceviri_ui import Ui_birimcevir
from uzunluk_ui import *
from kutle_ui import *
from direnc_ui import *
from kondansator_ui import *
from bobin_ui import *
from frekans_ui import *
from binary_ui import *
from ohmkurali_ui import *

#ANA MENÜYÜ AÇ
class anamenuPage(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.anaform = Ui_Anamenu()
        self.anaform.setupUi(self)
        self.birimceviriac = birimcevirPage()
        self.bilgiac = bilgiPage()
        self.anaform.pushButton_birimcevir.clicked.connect(self.birimceviriGiris)
        self.anaform.pushButton_bilgi.clicked.connect(self.bilgiGiris)
        self.anaform.pushButton_cikis.clicked.connect(self.close)
    def birimceviriGiris(self):
        self.close()
        self.birimceviriac.show()
    def bilgiGiris(self):
        self.close()
        self.bilgiac.show()


#BİLGİ MENÜSÜNÜ AÇ
class bilgiPage(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.bilgiform = Ui_bilgi()
        self.bilgiform.setupUi(self)
        self.bilgiform.pushButton_iuc.clicked.connect(self.linkIUC)
        self.bilgiform.pushButton_github.clicked.connect(self.linkGIT)
        self.bilgiform.pushButton_tbmyo.clicked.connect(self.linkTBMYO)
        self.bilgiform.pushButton_menuyedon_bilgi.clicked.connect(self.menuyeDon)
        self.bilgiform.pushButton_iuc.setToolTip("'iuc.edu.tr' sitesi açılacaktır.")
        self.bilgiform.pushButton_github.setToolTip("'github.com/turantem/birimcevirici' sitesi açılacaktır.")
        self.bilgiform.pushButton_tbmyo.setToolTip("'elektronikteknikbilimlermyo.iuc.edu.tr' sitesi açılacaktır")

    def linkIUC(self):
        url = 'https://iuc.edu.tr/'
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))

    def linkGIT(self):
        url = 'https://github.com/turantem/birimcevirici'
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))

    def linkTBMYO(self):
        url = 'https://elektronikteknikbilimlermyo.iuc.edu.tr'
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))

    def menuyeDon(self):
        self.close()
        self.menuac = anamenuPage()
        self.menuac.show()

#BİRİM ÇEVİRİ MENÜSÜNÜ AÇ
class birimcevirPage(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.birimcevirform = Ui_birimcevir()
        self.birimcevirform.setupUi(self)
        self.uzunlukac = uzunlukPage()
        self.kutleac = kutlePage()
        self.direncac = direncPage()
        self.kondansatorac = kondansatorPage()
        self.bobinac = bobinPage()
        self.frekansac = frekansPage()
        self.binaryac = binaryPage()
        self.ohmac = ohmPage()
        self.birimcevirform.pushButton_uzunluk.clicked.connect(self.uzunlukGiris)
        self.birimcevirform.pushButton_kutle.clicked.connect(self.kutleGiris)
        self.birimcevirform.pushButton_direnc.clicked.connect(self.direncGiris)
        self.birimcevirform.pushButton_kondansator.clicked.connect(self.kondansatorGiris)
        self.birimcevirform.pushButton_bobin.clicked.connect(self.bobinGiris)
        self.birimcevirform.pushButton_frekans.clicked.connect(self.frekansGiris)
        self.birimcevirform.pushButton_2to16.clicked.connect(self.binaryGiris)
        self.birimcevirform.pushButton_ohm.clicked.connect(self.ohmGiris)
        self.birimcevirform.pushButton_menuyedon.clicked.connect(self.menuyeDon)

    def bilgiGiris(self):
        self.close()
        self.bilgiac.show()

    def uzunlukGiris(self):
        self.close()
        self.uzunlukac.show()

    def kutleGiris(self):
        self.close()
        self.kutleac.show()

    def direncGiris(self):
        self.close()
        self.direncac.show()

    def kondansatorGiris(self):
        self.close()
        self.kondansatorac.show()

    def bobinGiris(self):
        self.close()
        self.bobinac.show()

    def frekansGiris(self):
        self.close()
        self.frekansac.show()

    def binaryGiris(self):
        self.close()
        self.binaryac.show()

    def ohmGiris(self):
        self.close()
        self.ohmac.show()

    def menuyeDon(self):
        self.close()
        self.menuac = anamenuPage()
        self.menuac.show()

#UZUNLUK SAYFASINI AÇ
class uzunlukPage(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.uzunlukform = Ui_uzunlukcevir()
        self.uzunlukform.setupUi(self)
        self.uzunlukform.pushButton_hesapla.clicked.connect(self.cevir)
        self.uzunlukform.pushButton_menuyedon_2.clicked.connect(self.menuyeDon2)
        self.uzunlukform.pushButton_bilgi.clicked.connect(self.bilgiVer)
        self.uzunlukform.pushButton_bilgi.setToolTip("Bu menüde uzunluğun birimi olan metre, alt ve üst katlarına çevrilebilir.")

    def menuyeDon2(self):
        self.close()
        self.birimceviriac = birimcevirPage()
        self.birimceviriac.show()

    def cevir(self):
        giris_birim = self.uzunlukform.comboBox_giris.currentText()
        cikis_birim = self.uzunlukform.comboBox_cikis.currentText()
        giris_text = self.uzunlukform.lineEdit_giris.text()

        # Kullanıcının giriş yapmadan hesaplama yapmaya çalışmasını kontrol et
        if not giris_text:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir miktar girin!")
            return

        miktar = float(giris_text)

        birimler = {
            "kilometre": 1000,
            "hektometre": 100,
            "dekametre": 10,
            "metre": 1,
            "desimetre": 0.1,
            "santimetre": 0.01,
            "milimetre": 0.001
        }

        try:
            faktor = birimler[giris_birim] / birimler[cikis_birim]
            sonuc = miktar * faktor
            if sonuc % 1 != 0:
                self.uzunlukform.lineEdit_cikis.setText("{:.8f}".format(sonuc))
            else:
                self.uzunlukform.lineEdit_cikis.setText(str(int(sonuc)))
        except ValueError:
            self.uzunlukform.lineEdit_cikis.setText("Geçersiz değer!")
        except ZeroDivisionError:
            self.uzunlukform.lineEdit_cikis.setText("Bölme sıfıra bölünemez!")

    def bilgiVer(self):
        QMessageBox.information(self, "Bilgi","Bu menüde uzunluğun birimi olan metre, alt ve üst katlarına çevrilebilir.")


#KÜTLE SAYFASINI AÇ
class kutlePage(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.kutleform = Ui_kutle()
        self.kutleform.setupUi(self)
        self.kutleform.pushButton_hesapla_kutle.clicked.connect(self.cevirkutle)
        self.kutleform.pushButton_menuyedon_kutle.clicked.connect(self.menuyeDon2)
        self.kutleform.pushButton_bilgi.clicked.connect(self.bilgiVer)
        self.kutleform.pushButton_bilgi.setToolTip("Bu menüde kütlenin birimi olan gram, alt ve üst katlarına çevrilebilir.")

    def cevirkutle(self):
        giris_birim = self.kutleform.comboBox_giris_kutle.currentText()
        cikis_birim = self.kutleform.comboBox_cikis_kutle.currentText()
        giris_text = self.kutleform.lineEdit_giris_kutle.text()

        # Kullanıcının giriş yapmadan hesaplama yapmaya çalışmasını kontrol et
        if not giris_text:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir miktar girin!")
            return

        miktar = float(giris_text)

        birimler = {
            "kilogram": 1000,
            "hektogram": 100,
            "dekagram": 10,
            "gram": 1,
            "desigram": 0.1,
            "santigram": 0.01,
            "miligram": 0.001
        }

        try:
            faktor = birimler[giris_birim] / birimler[cikis_birim]
            sonuc = miktar * faktor
            if sonuc % 1 != 0:
                self.kutleform.lineEdit_cikis_kutle.setText("{:.8f}".format(sonuc))
            else:
                self.kutleform.lineEdit_cikis_kutle.setText(str(int(sonuc)))
        except ValueError:
            self.kutleform.lineEdit_cikis_kutle.setText("Geçersiz değer!")
        except ZeroDivisionError:
            self.kutleform.lineEdit_cikis_kutle.setText("Bölme sıfıra bölünemez!")

    def menuyeDon2(self):
        self.close()
        self.birimceviriac = birimcevirPage()
        self.birimceviriac.show()

    def bilgiVer(self):
        QMessageBox.information(self, "Bilgi","Bu menüde kütlenin birimi olan gram, alt ve üst katlarına çevrilebilir.")

# DİRENÇ SAYFASINI AÇ
class direncPage(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.direncform = Ui_direnc()
        self.direncform.setupUi(self)
        self.direncform.radioButton_direncbirim.setChecked(True)
        self.direncform.radioButton_direncrenk.clicked.connect(self.showDirencRenk)
        self.direncform.radioButton_direncbirim.clicked.connect(self.showDirencBirim)
        self.direncform.comboBox_direncrenksec.currentIndexChanged.connect(self.bantSec)
        self.direncform.pushButton_menuyedon_direnc.clicked.connect(self.menuyeDon2)
        self.direncform.pushButton_bilgi.clicked.connect(self.bilgiVer)
        self.direncform.pushButton_bilgi.setToolTip("Bu menüde direncin birimi olan ohm, alt ve üst katlarına çevrilebilir. Ayrıca dirençlerin renk kodlarından değerleri bulunabilir.")

        self.direncform.pushButton_hesapla_direncbirim.clicked.connect(self.cevirdirenc)
        self.direncform.pushButton_hesapla_direncrenk_4bant.clicked.connect(self.renkdirenc4)
        self.direncform.pushButton_hesapla_direncrenk_5bant.clicked.connect(self.renkdirenc5)

    def showDirencRenk(self):
        self.direncform.stackedWidget.setCurrentWidget(self.direncform.direncrenk)

    def showDirencBirim(self):
        self.direncform.stackedWidget.setCurrentWidget(self.direncform.direncbirim)

    def bantSec(self, index):
        self.direncform.stackedWidget_direncrenk.setCurrentIndex(index)


    def cevirdirenc(self):
        giris_birim = self.direncform.comboBox_giris_direncbirim.currentText()
        cikis_birim = self.direncform.comboBox_cikis_direncbirim.currentText()
        giris_text = self.direncform.lineEdit_giris_direncbirim.text()

        # Kullanıcının giriş yapmadan hesaplama yapmaya çalışmasını kontrol et
        if not giris_text:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir miktar girin!")
            return

        miktar = float(giris_text)

        birimler = {
            "megaohm": 1000000,
            "kiloohm": 1000,
            "ohm": 1,
            "miliohm": 0.001,
            "mikroohm": 0.000001,
        }

        try:
            faktor = birimler[giris_birim] / birimler[cikis_birim]
            sonuc = miktar * faktor
            if sonuc % 1 != 0:
                self.direncform.lineEdit_cikis_direncbirim.setText("{:.8f}".format(sonuc))
            else:
                self.direncform.lineEdit_cikis_direncbirim.setText(str(int(sonuc)))
        except ValueError:
            self.direncform.lineEdit_cikis_direncbirim.setText("Geçersiz değer!")
        except ZeroDivisionError:
            self.direncform.lineEdit_cikis_direncbirim.setText("Bölme sıfıra bölünemez!")

    def renkdirenc4(self):
        renk_kodlari = {
            "Siyah": (0, 0, 0, 1),
            "Kahverengi": (1, 1, 10, 0.01),
            "Kırmızı": (2, 2, 100, 0.02),
            "Turuncu": (3, 3, 1000, 0.03),
            "Sarı": (4, 4, 10000, 0.04),
            "Yeşil": (5, 5, 100000, 0.005),
            "Mavi": (6, 6, 1000000, 0.0025),
            "Mor": (7, 7, 10000000, 0.001),
            "Gri": (8, 8, 100000000, 0.0005),
            "Beyaz": (9, 9, 1000000000, 0.002),
            "Altın": (None, None, 0.1, 0.05),
            "Gümüş": (None, None, 0.01, 0.1)
        }

        renk1 = self.direncform.comboBox_direncrenk1_4bant.currentText()
        renk2 = self.direncform.comboBox_direncrenk2_4bant.currentText()
        carpan_index = self.direncform.comboBox_carpan_4bant.currentIndex()
        tolerans_text = self.direncform.comboBox_tolerans_4bant.currentText()

        if carpan_index < 10:
            carpan = 10 ** carpan_index
        else:
            carpan = renk_kodlari[renk1][2]  # Altın veya Gümüş için çarpanı kullan

        if tolerans_text in renk_kodlari:
            tolerans = renk_kodlari[tolerans_text][3]  # Renk kodlarından toleransı al
        else:
            tolerans = 0  # Default olarak toleransı sıfır ata

        direnc_degeri = (renk_kodlari[renk1][0] * 10 + renk_kodlari[renk2][1]) * carpan

        min_deger = direnc_degeri - direnc_degeri * tolerans
        max_deger = direnc_degeri + direnc_degeri * tolerans

        # Toleransı düzgün bir şekilde biçimlendirerek göster
        if tolerans_text in ["Altın", "Gümüş"]:
            tolerans_metni = str(int(tolerans * 100))  # Yüzde değeri olarak göster, tamsayı olarak
        else:
            tolerans_metni = "{:.2f}".format(tolerans * 100)  # Yüzde değeri olarak göster, iki ondalık basamakla
        self.direncform.lineEdit_cikis_direncrenk_4bant.setText(
            f"{direnc_degeri} Ω")
        self.direncform.lineEdit_cikis_tolerans_4bant.setText(
            f"Tolerans: ±{tolerans_metni}%\n Min: {min_deger} Ω \nMax: {max_deger} Ω")

    def renkdirenc5(self):
        renk_kodlari = {
            "Siyah": (0, 0, 0, 1),
            "Kahverengi": (1, 1, 1, 10, 0.01),
            "Kırmızı": (2, 2, 2, 100, 0.02),
            "Turuncu": (3, 3, 3, 1000, 0.03),
            "Sarı": (4, 4, 4, 10000, 0.04),
            "Yeşil": (5, 5, 5, 100000, 0.005),
            "Mavi": (6, 6, 6, 1000000, 0.0025),
            "Mor": (7, 7, 7, 10000000, 0.001),
            "Gri": (8, 8, 8, 100000000, 0.0005),
            "Beyaz": (9, 9, 9, 1000000000, 0.002),
            "Altın": (None, None, None, 0.1, 0.05),
            "Gümüş": (None, None, None, 0.01, 0.1)
        }

        renk1 = self.direncform.comboBox_direncrenk1_5bant.currentText()
        renk2 = self.direncform.comboBox_direncrenk2_5bant.currentText()
        renk3 = self.direncform.comboBox_direncrenk3_5bant.currentText()
        carpan_index = self.direncform.comboBox_carpan_5bant.currentIndex()
        tolerans_text = self.direncform.comboBox_tolerans_5bant.currentText()

        if carpan_index < 10:
            carpan = 10 ** carpan_index
        else:
            carpan = renk_kodlari[renk1][3]  # Altın veya Gümüş için çarpanı kullan

        if tolerans_text in renk_kodlari:
            tolerans = renk_kodlari[tolerans_text][4]  # Renk kodlarından toleransı al
        else:
            tolerans = 0  # Default olarak toleransı sıfır ata

        direnc_degeri = (renk_kodlari[renk1][0] * 100 + renk_kodlari[renk2][1] * 10 + renk_kodlari[renk3][2]) * carpan

        min_deger = direnc_degeri - direnc_degeri * tolerans
        max_deger = direnc_degeri + direnc_degeri * tolerans

        # Toleransı düzgün bir şekilde biçimlendirerek göster
        if tolerans_text in ["Altın", "Gümüş"]:
            tolerans_metni = str(int(tolerans * 100))  # Yüzde değeri olarak göster, tamsayı olarak
        else:
            tolerans_metni = "{:.2f}".format(tolerans * 100)  # Yüzde değeri olarak göster, iki ondalık basamakla
        self.direncform.lineEdit_cikis_direncrenk_5bant.setText(
            f"{direnc_degeri} Ω")
        self.direncform.lineEdit_cikis_tolerans_5bant.setText(
            f"Tolerans: ±{tolerans_metni}%\n Min: {min_deger} Ω \nMax: {max_deger} Ω")

    def menuyeDon2(self):
        self.close()
        self.birimceviriac = birimcevirPage()
        self.birimceviriac.show()

    def bilgiVer(self):
        QMessageBox.information(self, "Bilgi","Bu menüde direncin birimi olan ohm, alt ve üst katlarına çevrilebilir. Ayrıca dirençlerin renk kodlarından değerleri bulunabilir.")

#KONDANSATÖR SAYFASINI AÇ
class kondansatorPage(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.kondansatorform = Ui_kondansator()
        self.kondansatorform.setupUi(self)
        self.kondansatorform.pushButton_hesapla_kondansator.clicked.connect(self.cevirkondansator)
        self.kondansatorform.pushButton_menuyedon_kondansator.clicked.connect(self.menuyeDon2)
        self.kondansatorform.pushButton_bilgi.clicked.connect(self.bilgiVer)
        self.kondansatorform.pushButton_bilgi.setToolTip("Bu menüde kondansatörün birimi olan farad, alt ve üst katlarına çevrilebilir.")

    def cevirkondansator(self):
        giris_birim = self.kondansatorform.comboBox_giris_kondansator.currentText()
        cikis_birim = self.kondansatorform.comboBox_cikis_kondansator.currentText()
        giris_text = self.kondansatorform.lineEdit_giris_kondansator.text()

        # Kullanıcının giriş yapmadan hesaplama yapmaya çalışmasını kontrol et
        if not giris_text:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir miktar girin!")
            return

        miktar = float(giris_text)

        birimler = {
            "farad": 100000000000,
            "microfarad": 100000000,
            "nanofarad": 100000,
            "picofarad": 1
        }

        try:
            faktor = birimler[giris_birim] / birimler[cikis_birim]
            sonuc = miktar * faktor
            if sonuc % 1 != 0:
                self.kondansatorform.lineEdit_cikis_kondansator.setText("{:.8f}".format(sonuc))
            else:
                self.kondansatorform.lineEdit_cikis_kondansator.setText(str(int(sonuc)))
        except ValueError:
            self.kondansatorform.lineEdit_cikis_kondansator.setText("Geçersiz değer!")
        except ZeroDivisionError:
            self.kondansatorform.lineEdit_cikis_kondansator.setText("Bölme sıfıra bölünemez!")

    def menuyeDon2(self):
        self.close()
        self.birimceviriac = birimcevirPage()
        self.birimceviriac.show()

    def bilgiVer(self):
        QMessageBox.information(self, "Bilgi","Bu menüde kondansatörün birimi olan farad, alt ve üst katlarına çevrilebilir.")

#BOBİN MENÜSÜNÜ AÇ
class bobinPage(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.bobinform = Ui_bobin()
        self.bobinform.setupUi(self)
        self.bobinform.pushButton_hesapla_bobin.clicked.connect(self.cevirbobin)
        self.bobinform.pushButton_menuyedon_bobin.clicked.connect(self.menuyeDon2)
        self.bobinform.pushButton_bilgi.clicked.connect(self.bilgiVer)
        self.bobinform.pushButton_bilgi.setToolTip("Bu menüde bobinin birimi olan Henry, alt ve üst katlarına çevrilebilir.")

    def cevirbobin(self):
        giris_birim = self.bobinform.comboBox_giris_bobin.currentText()
        cikis_birim = self.bobinform.comboBox_giris_bobin_2.currentText()
        giris_text = self.bobinform.lineEdit_giris_bobin.text()

        # Kullanıcının giriş yapmadan hesaplama yapmaya çalışmasını kontrol et
        if not giris_text:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir miktar girin!")
            return

        miktar = float(giris_text)

        birimler = {
            "gigahenry": 1000000000,
            "megahenry": 1000000,
            "kilohenry": 1000,
            "henry": 1,
            "milihenry": 0.001,
            "mikrohenry": 0.000001,
            "nanohenry": 0.000000001
        }

        try:
            faktor = birimler[giris_birim] / birimler[cikis_birim]
            sonuc = miktar * faktor
            if sonuc % 1 != 0:
                self.bobinform.lineEdit_cikis_bobin.setText("{:.8f}".format(sonuc))
            else:
                self.bobinform.lineEdit_cikis_bobin.setText(str(int(sonuc)))
        except ValueError:
            self.bobinform.lineEdit_cikis_bobin.setText("Geçersiz değer!")
        except ZeroDivisionError:
            self.bobinform.lineEdit_cikis_bobin.setText("Bölme sıfıra bölünemez!")
    def menuyeDon2(self):
        self.close()
        self.birimceviriac = birimcevirPage()
        self.birimceviriac.show()

    def bilgiVer(self):
        QMessageBox.information(self, "Bilgi","Bu menüde bobinin birimi olan Henry, alt ve üst katlarına çevrilebilir.")

#FREKANS MENÜSÜNÜ AÇ
class frekansPage(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.frekansform = Ui_frekans()
        self.frekansform.setupUi(self)
        self.frekansform.pushButton_hesapla_frekans.clicked.connect(self.cevirfrekans)
        self.frekansform.pushButton_menuyedon_frekans.clicked.connect(self.menuyeDon2)
        self.frekansform.pushButton_bilgi.clicked.connect(self.bilgiVer)
        self.frekansform.pushButton_bilgi.setToolTip("Girilen hertz değeri ışık hızının frekansa bölümüyle dalga boyuna çevrilir.")

    def cevirfrekans(self):
        # Giriş ve çıkış birimlerini al
        giris_birimi = self.frekansform.comboBox_giris_frekans.currentText()
        cikis_birimi = self.frekansform.comboBox_cikis_frekans.currentText()
        giris_text = self.frekansform.lineEdit_giris_frekans.text()

        # Kullanıcının giriş yapmadan hesaplama yapmaya çalışmasını kontrol et
        if not giris_text:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir miktar girin!")
            return

        miktar = float(giris_text)

        if miktar <= 0:
            raise ValueError("Frekans pozitif bir sayı olmalıdır.")

        # Dönüşüm faktörlerini tanımla
        frekans_birimleri = {
            "terahertz": 1e12,
            "gigahertz": 1e9,
            "megahertz": 1e6,
            "kilohertz": 1e3,
            "hertz": 1,
            "milihertz": 1e-3,
            "mikrohertz": 1e-6,
            "nanohertz": 1e-9,
            "pikohertz": 1e-12
        }

        uzunluk_birimleri = {
            "metre": 1,
            "milimetre": 1e-3,
            "mikrometre": 1e-6,
            "nanometre": 1e-9,
            "pikometre": 1e-12
        }

        try:
            frekans_hz = miktar * frekans_birimleri[giris_birimi]
            isik_hizi = 3 * 10 ** 8
            dalgaboyu_m = isik_hizi / frekans_hz
            sonuc = dalgaboyu_m / uzunluk_birimleri[cikis_birimi]
            if sonuc % 1 != 0:
                self.frekansform.lineEdit_cikis_frekans.setText("{:.8f}".format(sonuc))
            else:
                self.frekansform.lineEdit_cikis_frekans.setText(str(int(sonuc)))

        except ValueError:
            self.frekansform.lineEdit_cikis_frekans.setText("Geçersiz değer!")

        except ZeroDivisionError:
            self.frekansform.lineEdit_cikis_frekans.setText("Bölme sıfıra bölünemez!")

    def menuyeDon2(self):
        self.close()
        self.birimceviriac = birimcevirPage()
        self.birimceviriac.show()

    def bilgiVer(self):
        QMessageBox.information(self, "Bilgi","Girilen hertz değeri ışık hızının frekansa bölümüyle dalga boyuna çevrilir.")

#BINARY MENÜSÜNÜ AÇ
class binaryPage(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.binaryform = Ui_binary()
        self.binaryform.setupUi(self)
        #self.binaryform.pushButton_hesapla_binary.clicked.connect(self.cevirbinary) #İPTAL EDİLDİ
        self.binaryform.lineEdit_giris_binary.textChanged.connect(self.cevirbinary)
        self.binaryform.comboBox_giris_binary.currentIndexChanged.connect(self.cevirbinary)
        self.binaryform.comboBox_cikis_binary.currentIndexChanged.connect(self.cevirbinary)
        self.binaryform.pushButton_menuyedon_binary.clicked.connect(self.menuyeDon2)
        self.binaryform.pushButton_bilgi.clicked.connect(self.bilgiVer)
        self.binaryform.pushButton_bilgi.setToolTip("Kullanıcının girdiği decimal, binary, octal ve hexadecimal sayılar aynı şekilde; talebe göre 10lu, 8li, 2li, ve 16lı olarak yazdırılır.")

    def cevirbinary(self):
        input_text = self.binaryform.lineEdit_giris_binary.text()
        input_base = self.get_base(self.binaryform.comboBox_giris_binary.currentText())
        output_base = self.get_base(self.binaryform.comboBox_cikis_binary.currentText())

        try:
            if input_base == 2:
                decimal_value = int(input_text, 2)
            elif input_base == 8:
                decimal_value = int(input_text, 8)
            elif input_base == 16:
                decimal_value = int(input_text, 16)
            else:
                decimal_value = int(input_text)

            if output_base == 2:
                output_text = bin(decimal_value)[2:]
            elif output_base == 8:
                output_text = oct(decimal_value)[2:]
            elif output_base == 16:
                output_text = hex(decimal_value)[2:].upper()
            else:
                output_text = str(decimal_value)

            self.binaryform.lineEdit_cikis_binary.setText(output_text)

        except ValueError:
            self.binaryform.lineEdit_cikis_binary.setText("Gecersiz Giris")

        self.show()

    def get_base(self, text):
        if text == 'binary':
            return 2
        elif text == 'octal':
            return 8
        elif text == 'hexadecimal':
            return 16
        else:
            return 10

    def menuyeDon2(self):
        self.close()
        self.birimceviriac = birimcevirPage()
        self.birimceviriac.show()

    def bilgiVer(self):
        QMessageBox.information(self, "Bilgi","Kullanıcının girdiği decimal, binary, octal ve hexadecimal sayılar aynı şekilde; talebe göre 10lu, 8li, 2li, ve 16lı olarak yazdırılır.")


class ohmPage(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ohmform = Ui_ohm()
        self.ohmform.setupUi(self)
        self.ohmform.pushButton_hesapla_binary.clicked.connect(self.cevirohm)
        self.ohmform.pushButton_menuyedon_binary.clicked.connect(self.menuyeDon2)
        self.ohmform.pushButton_bilgi.clicked.connect(self.bilgiVer)
        self.ohmform.pushButton_bilgi.setToolTip("Bu menüde girdiğiniz iki değer kullanılarak, boş bıraktığını 3. değer bulunmaktadır. Bunun için V = I x R formülü kullanılmaktadır.")

    def cevirohm(self):
        try:
            if self.ohmform.lineEdit_volt.text() and self.ohmform.lineEdit_amper.text():
                V = float(self.ohmform.lineEdit_volt.text())
                I = float(self.ohmform.lineEdit_amper.text())
                R = V / I
                self.ohmform.lineEdit_ohm.setText(str(R))
            elif self.ohmform.lineEdit_volt.text() and self.ohmform.lineEdit_ohm.text():
                V = float(self.ohmform.lineEdit_volt.text())
                R = float(self.ohmform.lineEdit_ohm.text())
                I = V / R
                self.ohmform.lineEdit_amper.setText(str(I))
            elif self.ohmform.lineEdit_amper.text() and self.ohmform.lineEdit_ohm.text():
                I = float(self.ohmform.lineEdit_amper.text())
                R = float(self.ohmform.lineEdit_ohm.text())
                V = I * R
                self.ohmform.lineEdit_volt.setText(str(V))
        except (ValueError, ZeroDivisionError):
            pass

    def menuyeDon2(self):
        self.close()
        self.birimceviriac = birimcevirPage()
        self.birimceviriac.show()

    def bilgiVer(self):
        QMessageBox.information(self, "Bilgi", "Bu menüde girdiğiniz iki değer kullanılarak, boş bıraktığını 3. değer bulunmaktadır. Bunun için V = I x R formülü kullanılmaktadır.")
