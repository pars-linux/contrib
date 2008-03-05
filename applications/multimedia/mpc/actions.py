#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/Makefile.in", "srcTAG", "%s/samples" % get.srcTAG())
    pisitools.dosed("Makefile.in", "srcTAG", get.srcTAG())

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/mpc")
