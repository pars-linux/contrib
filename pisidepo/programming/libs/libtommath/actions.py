#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("-f makefile.shared")

def install():
    autotools.rawInstall("-f makefile.shared DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("changes.txt", "*.pdf")
