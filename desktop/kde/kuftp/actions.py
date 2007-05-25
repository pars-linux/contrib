#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    pisitools.domo("po/tr.po", "tr", "dolphin.mo")
    pisitools.domove("/usr/share/locale/*", "/usr/kde/3.5/share/locale/")
    kde.install()
