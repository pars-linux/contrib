#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    # change modes
    shelltools.chmod("%s/usr/lib/libxfce4menu*" % get.installDIR(), 0644)

    pisitools.dodoc("TODO", "THANKS", "README", "NEWS", "AUTHORS", "ChangeLog")
