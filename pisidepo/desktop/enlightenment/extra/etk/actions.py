#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="etk-20060926"

def setup():
    autotools.configure("--enable-nls \
                         --enable-rpath \
                         --with-evas \
                         --with-ecore \
                         --with-edje \
                         --with-libiconv \
                         --with-libintl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPING", "NEWS", "README", "TODO")
