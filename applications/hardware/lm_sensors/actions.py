#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pass

def build():
    shelltools.system("make user")

def install():
    shelltools.system("make DESTDIR=%s PREFIX=/usr MANDIR=/%s user_install" % (get.installDIR(),get.manDIR()))
    # remove conflict
    pisitools.remove("/usr/include/linux/i2c-dev.h")
    pisitools.dodoc("doc/lm_sensors-FAQ.html")