#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules

WorkDir = "protoeditor-1.1beta3"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    pythonmodules.fixCompiledPy(lookInto="%s/share/apps/protoeditor/libs/python" % get.kdeDIR())

    # Do not conflict with ktechlab.
    # These icons are also located in
    # /usr/kde/3.5/apps/protoeditor/icons.
    pisitools.removeDir("%s/share/icons/hicolor/22x22/actions" % get.kdeDIR())
