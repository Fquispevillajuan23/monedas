import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class Dialogo(QMainWindow):
    # Tipo de cambio 20240619
    USDtoPEN = 3.84
    USDtoEUR = 0.93
    USDtoBRL = 4.75  # Tasa de cambio dólar a reales brasileños
    EURtoPEN = 4.13  # Tasa de cambio euro a soles
    EURtoBRL = 5.10  # Tasa de cambio euro a reales brasileños
    BRLtoPEN = 0.82  # Tasa de cambio reales brasileños a soles

    def __init__(self):
        ruta = os.path.dirname(os.path.abspath(__file__)) + r"\..\vista\currencyConvert.ui"
        QMainWindow.__init__(self)
        uic.loadUi(ruta, self)

        self.pbTipoCambio.clicked.connect(self.calcularConversion)

    def calcularConversion(self):
        convertido = 0.0
        inicial = 0.0

        inicial = float(self.leImporte.text())
        convertido = inicial

        # Conversiones desde la moneda de origen a USD (dólares)
        if self.rbDeEUR.isChecked():
            convertido = inicial / self.USDtoEUR
        elif self.rbDePEN.isChecked():
            convertido = inicial / self.USDtoPEN
        elif self.rbDeBRL.isChecked():
            convertido = inicial / self.USDtoBRL

        # Conversiones desde USD (dólares) a la moneda de destino
        if self.rbAEUR.isChecked():
            convertido = convertido * self.USDtoEUR
        elif self.rbAPEN.isChecked():
            convertido = convertido * self.USDtoPEN
        elif self.rbABRL.isChecked():
            convertido = convertido * self.USDtoBRL
        elif self.rbAUSD.isChecked():
            convertido = convertido

        self.lblCambio.setText(f"{convertido:.2f}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = Dialogo()
    dialogo.show()
    app.exec_()
