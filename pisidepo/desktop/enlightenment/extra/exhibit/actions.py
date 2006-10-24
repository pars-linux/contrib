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

WorkDir="exhibit-20060926"

def setup():
    autotools.configure("--with-ecore \
                         --with-ecore-exec \
                         --with-evas \
                         --with-evas-exec \
                         --with-etk \
                         --with-etk-exec \
                         --with-edje \
                         --with-edje-exec \
                         --with-eet \
                         --with-eet-exec \
                         --with-engrave \
                         --with-engrave-exec \
                         --with-enlightenment \
                         --with-enlightenment-exec \
                         --with-epsilon \
                         --with-epsilon-exec")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "INSTALL", "README", "TODO")