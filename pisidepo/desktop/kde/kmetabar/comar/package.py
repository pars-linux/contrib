#!/usr/bin/python
#-*- coding: utf-8 -*-
#
# turkay.eren@gmail.com
#######################

import os

def postInstall():
    os.system("/usr/bin/wall Kmetabar paketi sisteme yuklendi! Kullanmak icin konqueror programini acin, sol taraftaki Gezgin Paneline sag tiklayip \" Yeni Ekle -> Kmetabar \" butonuna tiklayin")

def preRemove():
    os.system("/usr/bin/wall Kmetabar paketi sistemden kaldirildi! Konqueror programındaki simgesini kaldırmak icin sol taraftaki Gezgin Panelinden Kmetabar simgesine sag tiklayip \" Cikar \" butonunu tiklayin")
