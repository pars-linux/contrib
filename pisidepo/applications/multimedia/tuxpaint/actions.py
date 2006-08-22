#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir=""

def setup():
    shelltools.system("rpm2targz tuxpaint-0.9.15b-1.fc4.i386.rpm")
    shelltools.system("tar -zxvf tuxpaint-0.9.15b-1.fc4.i386.tar.gz")

def build():
    pass

def install():
    pisitools.insinto("/etc/tuxpaint", "etc/tuxpaint/*")
    pisitools.insinto("/usr/bin", "usr/bin/*")
    pisitools.insinto("/usr/share/applications/", "usr/share/applications/*")
    pisitools.insinto("/usr/share/icons/hicolor", "usr/share/icons/hicolor/*")
    pisitools.doman("usr/share/man/man1/*")
    pisitools.doman("usr/share/man/pl/man1/*")
    pisitools.insinto("/usr/share/pixmaps", "usr/share/pixmaps/*")
    pisitools.insinto("/usr/share/tuxpaint", "usr/share/tuxpaint/*")
    pisitools.dodoc("usr/share/doc/tuxpaint-0.9.15b/*.txt")

