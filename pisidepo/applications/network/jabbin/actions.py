#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Murat Şenel <muratasenel@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="jabbin-2.0beta"

def setup():
    pisitools.dosed("install.sh","INSTALL_PATH=\"/usr\"","INSTALL_PATH=\"%s/usr\"" % get.installDIR())
    shelltools.export("QTDIR", "%s" % get.qtDIR())

def build():
    shelltools.system("%s/bin/qmake -o Makefile jabbin.pro" % get.qtDIR())
    autotools.make()

def install():
    #autotools.install doesn't do the trick here :\
    shelltools.system("./install.sh")
    pisitools.insinto("/usr/share/applications", "jabbin.desktop")
    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "NEWS", "README")
