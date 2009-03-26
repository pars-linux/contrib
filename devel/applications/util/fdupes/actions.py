#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "-o fdupes", "%s -o fdupes" % get.CFLAGS())
    pisitools.dosed("Makefile", "gcc", "%s" % get.CC())

def build():
    autotools.make()

def install():
    pisitools.dobin("fdupes")
    pisitools.doman("fdupes.1")

    pisitools.dodoc("CONTRIBUTORS", "CHANGES", "README", "TODO")
