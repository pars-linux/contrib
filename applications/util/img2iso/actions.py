#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "isodump-0.05.02"

def setup():
    ###Name change http://wiki.linuxquestions.org/wiki/CD_Image_Conversion
    pisitools.dosed("isodump.c", "isodump", "img2iso")
    pisitools.dosed("isodump.h", "isodump", "img2iso")
    pisitools.dosed("Makefile.Linux", "isodump", "img2iso")
    pisitools.dosed("isodump.man", "isodump", "img2iso")
    #
    shelltools.move("isodump.c", "img2iso.c")
    shelltools.move("isodump.h", "img2iso.h")
    shelltools.move("isodump.man", "img2iso.man")
    ###

    autotools.configure()
 
def build():
    autotools.make()

def install():
    pisitools.dobin("img2iso")
    pisitools.doman("img2iso.man")
    pisitools.domove("/usr/share/man/manman/img2iso.man", "%s/man1" % get.manDIR(), "img2iso.1")
    pisitools.dodoc("ChangeLog", "COPYING", "INSTALL", "FORMATS.txt", "README", "TODO")
