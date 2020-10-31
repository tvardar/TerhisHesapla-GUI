# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from terhis import *
import datetime
import datedelta

uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui =Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()


# ----- HESAPLAMALAR -----


def SEVKTARIHI():
    ui.lb_girilen_tarih.setText(ui.tarih.text())

def SURE():
    tarih0 = ui.tarih.text().strip().split(".")
    sevk = datetime.datetime(int(tarih0[2]),int(tarih0[1]),int(tarih0[0]))
    now = datetime.datetime.now()
    sure = (now - sevk)
    ui.lb_gecen_sure.setText(str(sure.days))

def TERHIS():
    tarih0 = ui.tarih.text().strip().split(".")
    sevk = datetime.datetime(int(tarih0[2]), int(tarih0[1]), int(tarih0[0]))

    rapor = int(ui.rapor.text())

    izin = int(ui.k_izin.value())

    erken_terhis = int(ui.erken_terhis.text())

    yol = int(ui.yol.text())

    ceza = int(ui.ceza.text())

    gec_katilis = int(ui.gec_katilis.text())


    if rapor > 6:
        rapor -= 6
    else:
        rapor = 0

    if (izin <= 6):
        izin = (6 - izin)
    else:
        izin = izin

    uzat = gec_katilis + ceza + rapor

    kisalt = erken_terhis + yol + izin

    if uzat > kisalt:
        h1 = uzat - kisalt
        gun = h1
        sevk = datetime.datetime(int(tarih0[2]), int(tarih0[1]), int(tarih0[0])) + datedelta.datedelta(
            months=6) + datedelta.datedelta(days=gun)
    else:
        h1 = kisalt - uzat
        gun = h1
        sevk = datetime.datetime(int(tarih0[2]), int(tarih0[1]), int(tarih0[0])) + datedelta.datedelta(
            months=6) - datedelta.datedelta(days=gun)

    sevk2 = sevk
    x = (str(sevk2.day))+"."+(str(sevk2.month))+"."+(str(sevk2.year))

    ui.lb_terhis_tarih.setText(x)

ui.pushButton.clicked.connect(SEVKTARIHI)
ui.pushButton.clicked.connect(SURE)
ui.pushButton.clicked.connect(TERHIS)

sys.exit(uygulama.exec_())