#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

WorkDir="hamachi-0.9.9.9-20-lnx"

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pass

def build():
    pisitools.dosed("tuncfg/Makefile","/sbin","%s/usr/bin" % get.installDIR())
    pisitools.dosed("Makefile","/usr/bin","%s/usr/bin" % get.installDIR())
    pisitools.dosed("Makefile","/sbin","%s/usr/bin" % get.installDIR())

def install():
    shelltools.system("/usr/bin/mkdir -p %s/usr/bin" % get.installDIR())
    autotools.install()
    pisitools.dodoc("README","LICENSE")