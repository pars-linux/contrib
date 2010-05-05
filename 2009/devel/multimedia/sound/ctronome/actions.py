#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed("Makefile", "-c", "%s -c" % get.CFLAGS())
    pisitools.dosed("Makefile", "-o", "%s -o" % get.LDFLAGS())
    pisitools.dosed("Makefile", "^CC=.*", "CC=%s" % get.CC())
    autotools.make()

def install():
    pisitools.dobin("ctronome")
    pisitools.insinto("/usr/share/ctronome","*.wav")
    pisitools.dodoc("ChangeLog", "COPYING", "NOTES", "prog_example.txt", "README", "TODO")
