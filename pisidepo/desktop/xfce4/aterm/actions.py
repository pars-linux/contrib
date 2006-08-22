#!/usr/bin/python
#-*- coding: UTF-8 -*-
#
# turkay.eren@gmail.com
#######################

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-terminfo=/usr/share/terminfo \
                         --enable-transparency \
                         --enable-fading \
                         --enable-background-image \
                         --enable-menubar \
                         --enable-graphics \
                         --enable-utmp \
                         --enable-wtmp \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.doman("doc/aterm.1")
    pisitools.dodoc("ChangeLog.rxvt","doc/BUGS","doc/README.menu","doc/README.xvt","doc/menu/*")