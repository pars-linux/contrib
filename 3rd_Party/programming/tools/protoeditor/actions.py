#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "protoeditor-1.1beta3"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    # Do not conflict with ktechlab.
    # These icons are also located in
    # /usr/kde/3.5/apps/protoeditor/icons.
    pisitools.removeDir("%s/share/icons/hicolor/22x22/actions" % get.kdeDIR())
