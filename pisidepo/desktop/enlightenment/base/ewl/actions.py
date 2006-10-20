#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ewl-0.0.4.007"

def setup():
    autotools.configure("--with-evas \
                         --with-evas-exec \
                         --with-ecore \
                         --with-ecore-exec \
                         --with-emotion \
                         --with-emotion-exec \
                         --with-edje \
                         --with-edje-exec \
                         --with-x \
                         --enable-opengl \
                         --enable-fbcon")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "NEWS", "README", "TODO")