#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.


from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = "/"


def setup():
    shelltools.system("rpm2targz opera-8.54-20060330.6-shared-qt.i386-en.rpm")
    shelltools.system("tar -zxvf opera-8.54-20060330.6-shared-qt.i386-en.tar.gz")

def build():
    pass

def install():
    pisitools.insinto("/usr", "usr/*")
    pisitools.insinto("/etc", "etc/opera*")
    pisitools.removeDir("/usr/X11R6")
    pisitools.removeDir("/usr/share/bug")

#   Opera icons opera.xpm, opera_16x16.png, opera_22x22.png, opera_32x32.png, opera_48x48.png etc.
    pisitools.dosym("/usr/share/opera/images/opera.xpm", "/usr/share/pixmaps/opera.png")   