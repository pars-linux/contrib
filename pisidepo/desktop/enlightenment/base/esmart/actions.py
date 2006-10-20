#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="esmart-0.9.0.007"

def setup():
    autotools.configure("--with-evas \
                         --with-evas-exec \
                         --with-ecore \
                         --with-ecore-exec \
                         --with-imlib2 \
                         --with-imlib2-exec \
                         --with-epsilon \
                         --with-epsilon-exec \
                         --with-edje \
                         --with-edje-exec")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README")

