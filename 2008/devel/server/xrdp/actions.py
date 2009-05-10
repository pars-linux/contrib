#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.touch("./configure.ac")
    shelltools.touch("./NEWS")
    shelltools.touch("./AUTHORS")
    shelltools.touch("./README")
    shelltools.touch("./ChangeLog")
    autotools.autoreconf("-fvi")
    autotools.configure("--disable-static --localstatedir=/var")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.remove("/etc/xrdp/rsakeys.ini")
    pisitools.rename("/etc/pam.d/xrdp-sesman", "sesman")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
