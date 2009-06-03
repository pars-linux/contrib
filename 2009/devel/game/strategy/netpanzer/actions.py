#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-sdltest")

def build():
    shelltools.system("jam")

def install():
    shelltools.system("jam -sDESTDIR=%s \
                           -sappdocdir=/%s/%s \
                            install" %
                            (get.installDIR(), get.docDIR(), get.srcTAG()))

    pisitools.remove("/usr/share/pixmaps/netpanzer.xpm")
