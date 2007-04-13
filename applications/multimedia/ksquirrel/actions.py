#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde

WorkDir="ksquirrel-0.7.0-pre2"

def setup():
    kde.configure("--with-qt-dir=/usr/qt/3 \
                   --with-qt-includes=/usr/qt/3/include \
                   --with-qt-libraries=/usr/qt/3/lib")

def build():
    kde.make()

def install():
    kde.install()
