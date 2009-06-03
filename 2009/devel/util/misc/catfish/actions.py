#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr")
    pisitools.dosed("Makefile", "DESTDIR=", "DESTDIR=%s" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/doc/catfish")

    pisitools.dodoc("AUTHORS", "TODO", "ChangeLog", "COPYING", "README")
