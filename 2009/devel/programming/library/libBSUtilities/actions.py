#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "bsutilities-%s" % get.srcVERSION()

def setup():
    autotools.configure("LOKISRC=/usr/include/loki \
                         --disable-static")

def build():
    autotools.make()
    autotools.make("doc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("documentation/html")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
