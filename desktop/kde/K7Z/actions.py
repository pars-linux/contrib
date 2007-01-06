#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.export("KDEDIR", get.installDIR() + get.kdeDIR())

def build():
    shelltools.cd("Build")
    autotools.make("all")

def install():
    shelltools.cd("Build")
    # Let's help the lazy makefile
    pisitools.insinto("%s/bin" % get.kdeDIR(), "../Bin/K7Z.py")
    pisitools.dodir("%s/share/apps/konqueror/servicemenus" % get.kdeDIR())
    pisitools.dodir("%s/share/icons/hicolor/32x32/actions" % get.kdeDIR())

    autotools.rawInstall()

