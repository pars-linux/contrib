#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import get

def setup():
    pass

def build():
    scons.make()

def install():
#   scons.install()
    scons.install("PREFIX=%s/usr" % get.installDIR())

#   Compile clean up
#   shelltools.unlinkDir("/share")
#   shelltools.unlink("/bin/ldcpp")

#   pisitools.dosym("/usr/share/ldcpp/ldcpp", "/usr/bin/ldcpp")
    pisitools.insinto("/usr/share/ldcpp/", "ldcpp")
    pisitools.insinto("/usr/share/ldcpp/pixmaps/", "pixmaps/*.png")
    pisitools.insinto("/usr/share/ldcpp/glade/", "glade/*.glade")
    pisitools.insinto("/usr/share/ldcpp/doc/", "*.txt")

