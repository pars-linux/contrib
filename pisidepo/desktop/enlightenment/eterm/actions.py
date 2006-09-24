#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#muratasenel@gmail.com

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Eterm-0.9.4"

def setup():
    autotools.configure("--prefix=/usr \
                         --with-x \
                         --disable-mmx \
                         --disable-escreen \
                         --enable-etwin \
                         --enable-strict-icccm \
                         --enable-profile \
                         --enable-utmp \
                         --with-imlib \
                         --enable-trans \
                         --enable-auto-encoding \
                         --enable-name-reporting-escapes \
                         --enable-xim \
                         --enable-unicode-multi-charset \
                         --with-delete=execute \
                         --with-backspace=auto")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("Changelog", "README", "ReleaseNotes*", "bg/README.backgrounds")

