#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

#   conflict with /usr/kde/3.5/share/mimelnk/application/x-icq.desktop
    pisitools.removeDir("/usr/kde/3.5/share/mimelnk")
