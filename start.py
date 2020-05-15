# 7.	Třída Prekladac (překladač ve smyslu slovníku (např. zadá se zkratka DMR a program vypíše „Digitální model reliéfu“).
# Slovník si vytvoříte sami (stačí 5 položek).
# o	Metoda preloz z parametrem text
# o	Metoda prelozZpet z parametrem text
from PyQt5 import QtWidgets, uic  # import potrebnych kniznic
from PyQt5.QtWidgets import QListWidgetItem

from prekladac import Prekladac  # import triedy Prekladac zo suboru prekladac.py


class Gui:  # definovanie triedy
    okno = None
    prekladac = Prekladac()  # vytvarame objekt

    def nacitaj_slovnik(self):
        for i in iter(self.prekladac.slovnik):
            item = QListWidgetItem(f'{i} : {self.prekladac.slovnik[i]}')
            self.okno.slovnik.addItem(item)

    def prirad_okno(self, okno):
        self.okno = okno

    def hladaj_skratku(self):  # metoda na hladanie skratky
        vstupny_cely_nazov = self.okno.vstup_cely_nazov.text()  # z gui vyberame zadany nazov a uklada ho do premennej
        najdena_skratka = self.prekladac.hladanie_skratky(
            vstupny_cely_nazov)  # do premennej ukladame skratku, ktoru sme nasli na zaklade celeho nazvu
        self.okno.najdena_skratka.setText(najdena_skratka)  # vypise najdenu skratku do okna v gui

    def hladaj_nazov(self):
        vstupna_skratka = self.okno.vstup_skratka.text()
        najdeny_nazov = self.prekladac.hladanie_nazvu(vstupna_skratka)
        self.okno.najdeny_cely_nazov.setText(najdeny_nazov)


def start():
    app = QtWidgets.QApplication([])
    okno = QtWidgets.QDialog()
    with open('prekladac.ui') as f:
        uic.loadUi(f, okno)

    gui = Gui()
    gui.prirad_okno(okno)

    okno.hladaj_skratku.clicked.connect(gui.hladaj_skratku)
    okno.hladaj_cely_nazov.clicked.connect(gui.hladaj_nazov)
    gui.nacitaj_slovnik()
    okno.show()

    return app.exec()


start()
