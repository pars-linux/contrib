#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.domove("/usr/share/pkgconfig/gnome-icon-theme.pc","/usr/lib/pkgconfig")

    pisitools.dodoc("TODO", "README", "NEWS", "AUTHORS")
