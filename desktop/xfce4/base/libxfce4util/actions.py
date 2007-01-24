#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-static=no")

def build():
    autotools.make()


def install():
    autotools.install()
    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.dodoc("README", "NEWS", "TODO", "THANKS", "ChangeLog", "AUTHORS")