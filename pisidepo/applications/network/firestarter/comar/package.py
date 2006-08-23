#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# turkay.eren@gmail.com
#######################

import os

def postInstall():
    os.system("/usr/bin/chmod +x /etc/init.d/firestarter")
    os.system("/usr/bin/wall Firestarter basariyla kuruldu! Guvenlik duvarinin sistem baslangicinda otomatik olarak calismasini saglamak icin konsoldan su komutu ile root olup: rc-update add firestarter default yazmaniz yeterlidir.")

def preRemove():
    os.system("/usr/bin/wall Firestarter kaldirildi! Guvenlik duvarini sistem baslangicinda otomatik calismasini durdurmak icin konsoldan su komutu ile root olup: rc-update del firestarter default komutunu yazmaniz yeterlidir.")
