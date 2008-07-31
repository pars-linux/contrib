#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sh autogen.sh")
    autotools.configure("--disable-static \
                         --enable-imlib2 \
                         --enable-xinerama \
                         --enable-xft \
                         --enable-nls")

def build():
    autotools.make()

def install():
    pisitools.dosed("data/init", "bloe", "Solaris")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/fluxbox", "data/pixmaps")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
