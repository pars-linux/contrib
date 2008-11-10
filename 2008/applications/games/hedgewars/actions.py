#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir='hedgewars-src-%s' % get.srcVERSION()

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "QTfrontend/res/hh25x25.png", "hedgewars.png")

    pisitools.dodoc("COPYING", "README", "Fonts_LICENSE.txt")
    pisitools.doman("man/hedgewars.6")
