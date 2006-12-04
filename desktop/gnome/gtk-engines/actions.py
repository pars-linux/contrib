#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    #/usr/lib/pkgconfig/gtk-engines-2.pc from clearlooks package
    #/usr/lib/gtk-2.0/2.4.0/engines/libclearlooks.so from clearlooks package
    #/usr/lib/gtk-2.0/2.4.0/engines/libclearlooks.la from clearlooks package
    pisitools.remove("/usr/lib/pkgconfig/gtk-engines-2.pc")
    pisitools.remove("/usr/lib/gtk-2.0/2.4.0/engines/libclearlooks.so")
    pisitools.remove("/usr/lib/gtk-2.0/2.4.0/engines/libclearlooks.la")

    pisitools.dodoc("ChangeLog", "AUTHORS","NEWS", "README")
