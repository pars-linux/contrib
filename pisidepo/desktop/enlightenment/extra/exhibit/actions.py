#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="exhibit"

def setup():
    autotools.system("./autogen.sh --prefix=/usr \
                                   --with-ecore-prefix=/usr/share/ecore \
                                   --with-evas-prefix=/usr/share/evas \
                                   --with-edje-prefix=/usr/share/edje \
                                   --with-etk-prefix=/usr/share/etk \
                                   --with-epsilon-prefix=/use/share/epsilon \
                                   --with-engrave-prefix=/usr/share/engrave")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPING*", "NEWS", "README", "TODO")
