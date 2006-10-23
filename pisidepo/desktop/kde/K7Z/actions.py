#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir="."

def setup():
    shelltools.system("7z x %s.7z" % get.srcDIR())
    shelltools.export("KDEDIR", get.installDIR() + get.kdeDIR())

def build():
    shelltools.cd(get.srcDIR())
    autotools.make()

def install():
    shelltools.cd(get.srcDIR())
    # Let's help the lazy makefile
    pisitools.insinto("%s/bin" % get.kdeDIR(), "Bin/K7Z.py")
    pisitools.dodir("%s/share/apps/konqueror/servicemenus" % get.kdeDIR())
    pisitools.dodir("%s/share/icons/hicolor/32x32/actions" % get.kdeDIR())
    
    autotools.install()

