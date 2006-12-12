#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde

def setup():
    kde.configure("--with-qtdir=/usr/qt/3 --with-Qt-include-dir=/usr/qt/3/include --with-Qt-bin-dir=/usr/qt/3/bin --with-Qt-lib-dir=/usr/qt/3/lib")

def build():
    kde.make()

def install():
    kde.install() 
