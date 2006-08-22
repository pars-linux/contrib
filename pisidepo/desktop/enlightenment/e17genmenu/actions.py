#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="e17genmenu"

def setup():
    autotools.system("./autogen.sh --prefix=/usr \
                                   --with-ecore-prefix=/usr/share/ecore \
                                   --with-eet-exec-prefix=/usr/bin \
                                   --with-engrave=/usr/include/engrave")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING", "NEWS", "README", "TODO")
    pisitools.removeDir("/usr/doc")