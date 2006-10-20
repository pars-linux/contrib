#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="e17genmenu"

def setup():
    shelltools.system("./autogen.sh --prefix=/usr \
                                    --with-ecore \
                                    --with-ecore-exec \
                                    --with-eet \
                                    --with-eet-exec \
                                    --with-engrave \
                                    --with-engrave-exec")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/doc")
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING", "NEWS", "README", "TODO")