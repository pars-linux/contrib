#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="eclair-0.0.1"

def setup():
    autotools.system("./autogen.sh --prefix=/usr \
                                   --enable-xine \
                                   --disable-libtool-lock \
                                   --with-evas=/usr/share/evas \
                                   --with-emotion=/usr/lib/emotion \
                                   --with-gnu-ld \
                                   --with-pic")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")