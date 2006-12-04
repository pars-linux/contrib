#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure("--enable-debug=full")

def build():
    kde.make()

def install():
    kde.install()
    
#   conflict with /usr/kde/3.5/share/mimelnk/application/x-icq.desktop
    pisitools.removeDir("/usr/kde/3.5/share/mimelnk")