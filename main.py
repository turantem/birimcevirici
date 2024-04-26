from PyQt5.QtWidgets import QApplication
from menu import anamenuPage


app = QApplication([])
pencere = anamenuPage()
pencere.show()
app.exec_()